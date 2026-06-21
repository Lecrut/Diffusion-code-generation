def find_middle_value(nums):
    if not nums:
        raise ValueError("The list cannot be empty")
    
    def partition(low, high):
        pivot = nums[high]
        i = low - 1
        for j in range(low, high):
            if nums[j] <= pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1], nums[high] = nums[high], nums[i + 1]
        return i + 1

    def quickselect(low, high, k):
        if low == high:
            return nums[low]
        
        pivot_index = partition(low, high)
        
        if k == pivot_index:
            return nums[k]
        elif k < pivot_index:
            return quickselect(low, pivot_index - 1, k)
        else:
            return quickselect(pivot_index + 1, high, k)

    n = len(nums)
    return quickselect(0, n - 1, n // 2)

if __name__ == '__main__':
    sample_values = [7, 10, 4, 3, 20, 15]
    middle_value = find_middle_value(sample_values)
    print(middle_value)