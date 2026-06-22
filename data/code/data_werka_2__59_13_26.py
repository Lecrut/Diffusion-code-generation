def find_middle_value(nums):
    if not nums:
        raise ValueError("The list cannot be empty")
    
    def validate_input(lst):
        if not all(isinstance(x, int) for x in lst):
            raise ValueError("All elements in the list must be integers")
    
    validate_input(nums)
    
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
        
        pivot = median_of_three(nums[l], nums[r], nums[(l + r) // 2])
        i = j = l
        k = r
        
        while True:
            while nums[i] < pivot:
                i += 1
            while nums[k] > pivot:
                k -= 1
            
            if i >= k:
                break
            
            nums[i], nums[k] = nums[k], nums[i]
            i += 1
            k -= 1
        
        mid_index = len(nums) // 2
        if l <= mid_index <= k:
            return quickselect(l, k)
        elif k < mid_index:
            return quickselect(k + 1, r)
        else:
            return quickselect(l, k - 1)
    
    return quickselect(0, len(nums) - 1)

if __name__ == '__main__':
    sample_values = [7, 2, 9, 3, 5, 8, 6]
    middle_value = find_middle_value(sample_values)
    print(middle_value)