def sort_and_count(numbers):
    if not isinstance(numbers, list) or not all(isinstance(num, int) for num in numbers):
        raise ValueError("Input must be a list of integers.")
    
    def count_even_numbers(nums):
        return sum(1 for num in nums if num % 2 == 0)
    
    sorted_list = sorted(numbers)
    even_count = count_even_numbers(numbers)
    return sorted_list, even_count

if __name__ == '__main__':
    sample_values = [12, 34, 56, 78, 90, 23, 45, 67]
    result = sort_and_count(sample_values)
    print(result)