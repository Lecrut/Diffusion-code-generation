import random

def find_middle_value(numbers):
    if not numbers:
        raise ValueError("List must not be empty")
    
    n = len(numbers)
    if n % 2 == 1:
        return _quickselect(numbers, n // 2)
    else:
        left = _quickselect(numbers, n // 2 - 1)
        right = _quickselect(numbers, n // 2)
        return (left + right) / 2.0

def _quickselect(arr, k):
    arr_copy = list(arr)
    left = 0
    right = len(arr_copy) - 1
    
    while left <= right:
        pivot_index = _partition(arr_copy, left, right)
        if pivot_index == k:
            return arr_copy[k]
        elif pivot_index < k:
            left = pivot_index + 1
        else:
            right = pivot_index - 1
            
    return arr_copy[k]

def _partition(arr, low, high):
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    pivot = arr[high]
    
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

if __name__ == '__main__':
    sample_list = [7, 10, 4, 3, 20, 15]
    result = find_middle_value(sample_list)
    print(result)