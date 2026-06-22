def validate_numbers(numbers):
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("All elements in the tuple must be numbers")

def product_of_tuple(numbers):
    validate_numbers(numbers)
    result = 1
    for number in numbers:
        result *= number
    return result

if __name__ == '__main__':
    sample_values = (2, 3, 4)
    print(product_of_tuple(sample_values))