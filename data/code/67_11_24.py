def validate_input(nums):
    if len(nums) < 2:
        raise ValueError('List must contain at least two elements')

def find_max_and_min(nums):
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
    return max1, max2, min1, min2

def max_product_pair(nums):
    validate_input(nums)
    max1, max2, min1, min2 = find_max_and_min(nums)
    return max(max1 * max2, min1 * min2)

if __name__ == '__main__':
    sample_values = [3, -1, 4, -1, 5]
    print(max_product_pair(sample_values))