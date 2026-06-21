def max_product_pair(nums):
    if len(nums) < 2:
        raise ValueError('List must contain at least two elements')
    
    MAX_FLOAT = float('inf')
    MIN_FLOAT = float('-inf')
    
    max1 = max2 = MIN_FLOAT
    min1 = min2 = MAX_FLOAT
    
    for num in nums:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2:
            max2 = num
        
        if num < min1:
            min2 = min1
            min1 = num
        elif num < min2:
            min2 = num
    
    return max(max1 * max2, min1 * min2)

if __name__ == '__main__':
    sample_values = [3, 5, -10, 7, -3]
    result = max_product_pair(sample_values)
    print(result)