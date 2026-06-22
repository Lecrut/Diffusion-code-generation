def filter_and_double_evens(numbers):
    if not all(isinstance(x, int) for x in numbers):
        raise ValueError("All elements in the list must be integers.")
    
    even_numbers = [num for num in numbers if num % 2 == 0]
    return even_numbers * 2

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 6]
    result = filter_and_double_evens(sample_list)
    print(result)