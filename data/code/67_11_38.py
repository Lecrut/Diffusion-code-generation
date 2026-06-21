def max_product_pair(nums):
    if len(nums) < 2:
        raise ValueError('List must contain at least two elements')
    
    def update_max_two(max1, max2, num):
        if num > max1:
            return num, max1
        elif num > max2:
            return max1, num
        return max1, max2
    
    def update_min_two(min1, min2, num):
        if num < min1:
            return num, min1
        elif num < min2:
            return min1, num
        return min1, min2
    
    max1 = max2 = float('-inf')
    min1 = min2 = float('inf')
    
    for num in nums:
        max1, max2 = update_max_two(max1, max2, num)
        min1, min2 = update_min_two(min1, min2, num)
    
    return max(max1 * max2, min1 * min2)

if __name__ == '__main__':
    sample_values = [1, 10, -5, 1, -100]
    print(max_product_pair(sample_values))