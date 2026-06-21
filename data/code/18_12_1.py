def find_median_index(values):
    if not values:
        raise ValueError("List must not be empty")
    
    n = len(values)
    target_index = n // 2
    
    def partition(arr, left, right, pivot_index):
        pivot_value = arr[pivot_index]
        arr[pivot_index], arr[right] = arr[right], arr[pivot_index]
        store_index = left
        for i in range(left, right):
            if arr[i] < pivot_value:
                arr[store_index], arr[i] = arr[i], arr[store_index]
                store_index += 1
        arr[store_index], arr[right] = arr[right], arr[store_index]
        return store_index
    
    def select(arr, left, right, k):
        if left == right:
            return left
        
        pivot_index = left + (right - left) // 2
        pivot_index = partition(arr, left, right, pivot_index)
        
        if k == pivot_index:
            return k
        elif k < pivot_index:
            return select(arr, left, pivot_index - 1, k)
        else:
            return select(arr, pivot_index + 1, right, k)
    
    select(values.copy(), 0, n - 1, target_index)
    
    if n % 2 == 1:
        return target_index
    else:
        left_med = select(values.copy(), 0, n - 1, target_index - 1)
        return left_med

if __name__ == '__main__':
    sample_list1 = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    print(find_median_index(sample_list1))
    
    sample_list2 = [7, 3, 9, 1, 5]
    print(find_median_index(sample_list2))
    
    sample_list3 = [10, 20, 30, 40]
    print(find_median_index(sample_list3))