def sort_and_count(numbers):
    if not isinstance(numbers, list) or not all(isinstance(num, int) for num in numbers):
        raise ValueError("Input must be a list of integers.")
    
    def is_even(num):
        return num % 2 == 0
    
    sorted_numbers = sorted(numbers)
    even_count = sum(is_even(num) for num in numbers)
    return sorted_numbers, even_count

if __name__ == '__main__':
    sample_values = [12, 3, 7, 6, 4, 8, 2, 5]
    result = sort_and_count(sample_values)
    print(result)