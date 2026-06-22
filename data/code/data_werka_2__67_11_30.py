def max_product_pair(nums):
    if len(nums) < 2:
        raise ValueError('List must contain at least two elements')
    largest = second_largest = float('-inf')
    smallest = second_smallest = float('inf')
    for num in nums:
        if num > largest:
            second_largest, largest = (largest, num)
        elif num > second_largest:
            second_largest = num
        if num < smallest:
            second_smallest, smallest = (smallest, num)
        elif num < second_smallest:
            second_smallest = num
    return max(largest * second_largest, smallest * second_smallest)
if __name__ == '__main__':
    sample_values = [1, 10, -5, 1, -100]
    result = max_product_pair(sample_values)
    print(result)