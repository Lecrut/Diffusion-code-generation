def find_middle_value(nums):
    if not nums:
        raise ValueError("The list cannot be empty")
    
    def median_of_three(a, b, c):
        if (a > b and a < c) or (a < b and a > c):
            return a
        elif (b > a and b < c) or (b < a and b > c):
            return b
        else:
            return c
    
    def quickselect(l, r):
        if l == r:
            return nums[l]
        
        pivot_index = partition(l, r)
        if pivot_index == len(nums) // 2:
            return nums[pivot_index]
        elif pivot_index < len(nums) // 2:
            return quickselect(pivot_index + 1, r)
        else:
            return quickselect(l, pivot_index - 1)
    
    def partition(l, r):
        pivot = median_of_three(nums[l], nums[r], nums[(l + r) // 2])
        i = l
        for j in range(l, r):
            if nums[j] < pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        nums[i], nums[r] = nums[r], nums[i]
        return i
    
    return quickselect(0, len(nums) - 1)

if __name__ == '__main__':
    sample_values = [7, 2, 5, 3, 8, 6, 4]
    middle_value = find_middle_value(sample_values)
    print(middle_value)