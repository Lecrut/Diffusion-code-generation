def find_middle_value(nums):
    if not nums:
        raise ValueError("The list cannot be empty")
    
    def validate_input(nums):
        if not isinstance(nums, list) or not all(isinstance(x, int) for x in nums):
            raise ValueError("Input must be a list of integers")

    validate_input(nums)
    
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

    mid_index = len(nums) // 2
    return quickselect(0, len(nums) - 1, mid_index)

if __name__ == '__main__':
    sample_values = [7, 2, 9, 4, 3, 6, 5]
    middle_value = find_middle_value(sample_values)
    print(middle_value)