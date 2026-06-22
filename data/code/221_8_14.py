def validate_numbers(numbers):
    if not isinstance(numbers, list) or len(numbers) != 3:
        raise ValueError("Input must be a list of exactly three numbers")

def order_numbers(numbers):
    validate_numbers(numbers)
    return sorted(numbers)

if __name__ == '__main__':
    sample_numbers = [42, 17, 9]
    print(order_numbers(sample_numbers))