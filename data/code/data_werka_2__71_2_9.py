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
        return (left + right) / 2.0

def _select_kth(nums, k):
    arr = list(nums)
    left = 0
    right = len(arr) - 1
    
    while True:
        if left == right:
            return arr[left]
        
        pivot_index = _partition(arr, left, right)
        
        if k == pivot_index:
            return arr[k]
        elif k < pivot_index:
            right = pivot_index - 1
        else:
            left = pivot_index + 1

def _partition(arr, left, right):
    pivot_index = random.randint(left, right)
    pivot_value = arr[pivot_index]
    
    arr[pivot_index], arr[right] = arr[right], arr[pivot_index]
    
    store_index = left
    for i in range(left, right):
        if arr[i] < pivot_value:
            arr[store_index], arr[i] = arr[i], arr[store_index]
            store_index += 1
            
    arr[store_index], arr[right] = arr[right], arr[store_index]
    
    return store_index

if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    result = find_middle_value(sample_list)
    print(result)