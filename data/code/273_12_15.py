def filter_and_double_evens(numbers):
    if not isinstance(numbers, list) or not all(isinstance(num, int) for num in numbers):
        raise ValueError("Input must be a list of integers")
    
    even_numbers = [num for num in numbers if num % 2 == 0]
    return even_numbers * 2

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = filter_and_double_evens(sample_values)
    print(result)