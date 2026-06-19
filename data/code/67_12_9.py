def max_product_pair(nums):
    if len(nums) < 2:
        raise ValueError('List must contain at least two elements')
    
    MAX1 = MAX2 = float('-inf')
    MIN1 = MIN2 = float('inf')
    
    for num in nums:
        if num > MAX1:
            MAX2 = MAX1
            MAX1 = num
        elif num > MAX2:
            MAX2 = num
        
        if num < MIN1:
            MIN2 = MIN1
            MIN1 = num
        elif num < MIN2:
            MIN2 = num
    
    return max(MAX1 * MAX2, MIN1 * MIN2)

if __name__ == '__main__':
    sample_values = [3, 6, -2, -5, 7, 3]
    result = max_product_pair(sample_values)
    print(result)