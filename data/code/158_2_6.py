def validate_input(numbers):
    if not all(isinstance(num, int) for num in numbers):
        raise ValueError("All elements in the list must be integers.")

def filter_even_numbers(numbers):
    validate_input(numbers)
    return list(filter(lambda x: x % 2 == 0, numbers))

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_numbers = filter_even_numbers(sample_values)
    print(even_numbers)