# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#   配列のうち、連続する部分で最大になる部分配列を分割統治によって求める
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def find_maximum_subarray(A, low, high):
    
    if low == high: # 要素が一つしかない
        return low, high, A[low]
    else:
        mid = (low + high) // 2
        left_low, left_high, left_sum = find_maximum_subarray(A, low, mid) # 左の部分配列中で最大値をとる部分配列
        right_low, right_high, right_sum = find_maximum_subarray(A, mid+1, high) # 右の部分配列中で最大値をとる部分配列
        cross_low, cross_high, cross_sum = find_max_crossing_subarray(A, low, mid, high) # 最大値をとる部分配列が左右の部分配列に跨る場合
        
        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_low, left_high, left_sum
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum

def find_max_crossing_subarray(A, low, mid, high):
    
    left_sum = -100000000000
    right_sum = -100000000000
    left_idx = mid
    right_idx = mid+1
    tmp = 0
    for _ in range(len(A[:mid+1])):
        tmp += A[left_idx]
        if tmp > left_sum:
            left_sum = tmp
            max_left = left_idx
        left_idx -= 1
    tmp = 0
    for _ in range(len(A[mid+1:])):
        tmp += A[right_idx]
        if tmp > right_sum:
            right_sum = tmp
            max_right = right_idx
        right_idx += 1
    
    return max_left, max_right, left_sum+right_sum

A = [-10, 3, 24, 214, -100, 42, 40]

print(find_maximum_subarray(A, 0, len(A)-1))