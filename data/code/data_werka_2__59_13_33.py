def find_middle_value(nums):
    if not nums:
        raise ValueError("The list cannot be empty")
    
    def quickselect(arr, low, high, k):
        if low == high:
            return arr[low]
        
        pivot_index = partition(arr, low, high)
        
        if k == pivot_index:
            return arr[k]
        elif k < pivot_index:
            return quickselect(arr, low, pivot_index - 1, k)
        else:
            return quickselect(arr, pivot_index + 1, high, k)
    
    def partition(arr, low, high):
        pivot = arr[high]
        i = low
        for j in range(low, high):
            if arr[j] <= pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[i], arr[high] = arr[high], arr[i]
        return i
    
    mid_index = len(nums) // 2
    return quickselect(nums, 0, len(nums) - 1, mid_index)

if __name__ == '__main__':
    sample_values = [7, 3, 8, 9, 2, 5, 6]
    middle_value = find_middle_value(sample_values)
    print(middle_value)