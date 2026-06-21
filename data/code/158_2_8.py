def validate_input(numbers):
    if not all(isinstance(num, int) for num in numbers):
        raise ValueError("All elements must be integers")
    return numbers

def filter_even_numbers(numbers):
    validated_numbers = validate_input(numbers)
    return list(filter(lambda x: x % 2 == 0, validated_numbers))

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_numbers = filter_even_numbers(sample_values)
    print(even_numbers)