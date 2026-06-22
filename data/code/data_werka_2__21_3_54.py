def sort_and_count(numbers):
    def validate_input(nums):
        if not isinstance(nums, list) or not all(isinstance(num, int) for num in nums):
            raise ValueError("Input must be a list of integers.")
    
    def count_evens(nums):
        return sum(1 for num in nums if num % 2 == 0)
    
    validate_input(numbers)
    sorted_numbers = sorted(numbers)
    even_count = count_evens(numbers)
    return sorted_numbers, even_count

if __name__ == '__main__':
    sample_values = [4, 3, 8, 6, 1, 7, 2, 5]
    result = sort_and_count(sample_values)
    print(result)