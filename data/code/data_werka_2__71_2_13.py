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

def _select_kth(arr, k):
    arr_copy = list(arr)
    return _quickselect(arr_copy, 0, len(arr_copy) - 1, k)

def _quickselect(arr, left, right, k):
    if left == right:
        return arr[left]
    
    pivot_index = _partition(arr, left, right)
    
    if k == pivot_index:
        return arr[k]
    elif k < pivot_index:
        return _quickselect(arr, left, pivot_index - 1, k)
    else:
        return _quickselect(arr, pivot_index + 1, right, k)

def _partition(arr, left, right):
    pivot_index = random.randint(left, right)
    pivot_value = arr[pivot_index]
    arr[pivot_index], arr[right] = arr[right], arr[pivot_index]
    
    store_index = left
    for i in range(left, right):
        if arr[i] < pivot_value:
            arr[store_index], arr[i] = arr[i], arr[store_index]
            store_index += 1
    
    arr[right], arr[store_index] = arr[store_index], arr[right]
    return store_index

if __name__ == '__main__':
    sample_list = [7, 10, 4, 3, 20, 15]
    result = find_middle_value(sample_list)
    print(result)
    
    sample_list_odd = [1, 3, 5, 7, 9]
    result_odd = find_middle_value(sample_list_odd)
    print(result_odd)
    
    sample_list_even = [1, 2, 3, 4]
    result_even = find_middle_value(sample_list_even)
    print(result_even)