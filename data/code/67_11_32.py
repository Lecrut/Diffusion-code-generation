def max_product_pair(nums):
    if len(nums) < 2:
        raise ValueError('List must contain at least two elements')
    
    def find_two_largest(numbers):
        first = second = float('-inf')
        for num in numbers:
            if num > first:
                second = first
                first = num
            elif num > second:
                second = num
        return first, second
    
    def find_two_smallest(numbers):
        first = second = float('inf')
        for num in numbers:
            if num < first:
                second = first
                first = num
            elif num < second:
                second = num
        return first, second
    
    largest1, largest2 = find_two_largest(nums)
    smallest1, smallest2 = find_two_smallest(nums)
    
    return max(largest1 * largest2, smallest1 * smallest2)

if __name__ == '__main__':
    sample_values = [3, 6, -2, -5, 7, 3]
    print(max_product_pair(sample_values))