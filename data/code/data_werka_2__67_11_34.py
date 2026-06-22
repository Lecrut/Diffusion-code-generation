def max_product_pair(nums):
    if len(nums) < 2:
        raise ValueError('List must contain at least two elements')

    def find_two_largest_and_smallest(nums):
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
        return ((largest, second_largest), (smallest, second_smallest))
    (max1, max2), (min1, min2) = find_two_largest_and_smallest(nums)
    return max(max1 * max2, min1 * min2)
if __name__ == '__main__':
    sample_values = [1, 10, -5, 1, -100]
    print(max_product_pair(sample_values))