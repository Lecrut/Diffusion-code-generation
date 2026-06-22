def find_middle_value(numbers):
    if not numbers:
        raise ValueError("List must not be empty")
    
    n = len(numbers)
    if n % 2 == 1:
        return _select_kth(numbers, n // 2)
    else:
        left = _select_kth(numbers, n // 2 - 1)
        right = _select_kth(numbers, n // 2)
        return (left + right) / 2.0

def _select_kth(numbers, k):
    nums = list(numbers)
    low = 0
    high = len(nums) - 1
    target_index = k
    
    while low <= high:
        pivot_index = _partition(nums, low, high)
        if pivot_index == target_index:
            return nums[pivot_index]
        elif pivot_index < target_index:
            low = pivot_index + 1
        else:
            high = pivot_index - 1
            
    return nums[low]

def _partition(nums, low, high):
    pivot = nums[high]
    i = low - 1
    
    for j in range(low, high):
        if nums[j] <= pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
            
    nums[i + 1], nums[high] = nums[high], nums[i + 1]
    return i + 1

if __name__ == '__main__':
    sample_list = [7, 1, 3, 5, 9, 2, 4, 6, 8]
    result = find_middle_value(sample_list)
    print(result)
    
    sample_list_even = [10, 20, 30, 40]
    result_even = find_middle_value(sample_list_even)
    print(result_even)