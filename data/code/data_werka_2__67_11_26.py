def max_product_pair(nums):
    if len(nums) < 2:
        raise ValueError('List must contain at least two elements')
    
    def find_max_two(nums):
        first, second = float('-inf'), float('-inf')
        for num in nums:
            if num > first:
                first, second = num, first
            elif num > second:
                second = num
        return first, second

    def find_min_two(nums):
        first, second = float('inf'), float('inf')
        for num in nums:
            if num < first:
                first, second = num, first
            elif num < second:
                second = num
        return first, second

    max1, max2 = find_max_two(nums)
    min1, min2 = find_min_two(nums)

    return max(max1 * max2, min1 * min2)

if __name__ == '__main__':
    sample_values = [1, 10, -5, 1, -100]
    print(max_product_pair(sample_values))