def find_middle_value(nums):
    if not nums:
        raise ValueError("The list cannot be empty")
    
    def validate_input(nums):
        if not all(isinstance(x, int) for x in nums):
            raise TypeError("All elements must be integers")
    
    def partition(low, high):
        pivot = nums[high]
        i = low - 1
        for j in range(low, high):
            if nums[j] <= pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1], nums[high] = nums[high], nums[i + 1]
        return i + 1
    
    def quickselect(low, high):
        if low == high:
            return nums[low]
        
        pivot_index = partition(low, high)
        
        if pivot_index == len(nums) // 2:
            return nums[pivot_index]
        elif pivot_index < len(nums) // 2:
            return quickselect(pivot_index + 1, high)
        else:
            return quickselect(low, pivot_index - 1)
    
    validate_input(nums)
    return quickselect(0, len(nums) - 1)

if __name__ == '__main__':
    sample_values = [7, 2, 5, 3, 8, 6, 4]
    middle_value = find_middle_value(sample_values)
    print(middle_value)