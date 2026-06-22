def max_product_pair(nums):
    if len(nums) < 2:
        raise ValueError('List must contain at least two elements')
    max_values = [float('-inf')] * 2
    min_values = [float('inf')] * 2
    for num in nums:
        if num > max_values[0]:
            max_values[1] = max_values[0]
            max_values[0] = num
        elif num > max_values[1]:
            max_values[1] = num
        if num < min_values[0]:
            min_values[1] = min_values[0]
            min_values[0] = num
        elif num < min_values[1]:
            min_values[1] = num
    return max(max_values[0] * max_values[1], min_values[0] * min_values[1])
if __name__ == '__main__':
    sample_values = [1, 10, -5, 1, -100]
    result = max_product_pair(sample_values)
    print(result)