def max_product_pair(nums):
    if len(nums) < 2:
        raise ValueError('List must contain at least two elements')
    
    def find_two_largest(nums):
        first, second = float('-inf'), float('-inf')
        for num in nums:
            if num > first:
                second = first
                first = num
            elif num > second:
                second = num
        return first, second
    
    def find_two_smallest(nums):
        first, second = float('inf'), float('inf')
        for num in nums:
            if num < first:
                second = first
                first = num
            elif num < second:
                second = num
        return first, second
    
    max1, max2 = find_two_largest(nums)
    min1, min2 = find_two_smallest(nums)
    
    return max(max1 * max2, min1 * min2)

if __name__ == '__main__':
    sample_values = [1, 10, -5, 1, -100]
    result = max_product_pair(sample_values)
    print(result)