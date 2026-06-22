def validate_input(numbers):
    if not isinstance(numbers, tuple) or not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("Input must be a tuple of numbers")

def product_of_tuple(numbers):
    validate_input(numbers)
    result = 1
    for number in numbers:
        result *= number
    return result

if __name__ == '__main__':
    sample_values = (2, 3, 4)
    print(product_of_tuple(sample_values))