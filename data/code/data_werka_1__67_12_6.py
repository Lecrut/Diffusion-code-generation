def validate_input(nums):
    if not isinstance(nums, list):
        raise TypeError('Input must be a list')
    if len(nums) < 2:
        raise ValueError('List must contain at least two elements')

def find_max_and_min_pair(nums):
    max1 = max2 = float('-inf')
    min1 = min2 = float('inf')
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
    return (max1, max2), (min1, min2)

def max_product_pair(nums):
    validate_input(nums)
    max_pair, min_pair = find_max_and_min_pair(nums)
    return max(max_pair[0] * max_pair[1], min_pair[0] * min_pair[1])

if __name__ == '__main__':
    sample_values = [1, 10, -5, 1, -100]
    result = max_product_pair(sample_values)
    print(result)