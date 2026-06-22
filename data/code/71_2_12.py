import random

def find_middle_value(numbers):
    if not numbers:
        raise ValueError("List must not be empty")
    
    n = len(numbers)
    if n % 2 == 1:
        return _select_kth(numbers, n // 2)
    else:
        left = _select_kth(numbers, n // 2 - 1)
        right = _select_kth(numbers, n // 2)
        return (left + right) / 2

def _select_kth(nums, k):
    if len(nums) == 1:
        return nums[0]
    
    pivot = nums[len(nums) // 2]
    lows = [x for x in nums if x < pivot]
    highs = [x for x in nums if x > pivot]
    pivots = [x for x in nums if x == pivot]
    
    if k < len(lows):
        return _select_kth(lows, k)
    elif k < len(lows) + len(pivots):
        return pivots[0]
    else:
        return _select_kth(highs, k - len(lows) - len(pivots))

if __name__ == '__main__':
    sample_list = [7, 1, 3, 5, 9, 2, 8, 4, 6]
    result = find_middle_value(sample_list)
    print(result)
    
    sample_list_even = [10, 20, 30, 40]
    result_even = find_middle_value(sample_list_even)
    print(result_even)