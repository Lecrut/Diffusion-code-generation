def filter_even_numbers(numbers):
    if not all(isinstance(n, int) for n in numbers):
        raise ValueError("All elements in the list must be integers.")
    
    return [n for n in numbers if n % 2 == 0]

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(filter_even_numbers(sample_values))