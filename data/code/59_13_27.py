def find_middle_value(nums):
    if not nums:
        raise ValueError("The list cannot be empty")
    
    def quickselect(l, r, k):
        if l == r:
            return nums[l]
        
        pivot_index = partition(l, r)
        
        if k == pivot_index:
            return nums[k]
        elif k < pivot_index:
            return quickselect(l, pivot_index - 1, k)
        else:
            return quickselect(pivot_index + 1, r, k)
    
    def partition(low, high):
        pivot = nums[high]
        i = low
        for j in range(low, high):
            if nums[j] < pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        nums[i], nums[high] = nums[high], nums[i]
        return i
    
    return quickselect(0, len(nums) - 1, len(nums) // 2)

if __name__ == '__main__':
    sample_values = [7, 3, 5, 9, 1, 4, 6, 8, 2]
    middle_value = find_middle_value(sample_values)
    print(middle_value)