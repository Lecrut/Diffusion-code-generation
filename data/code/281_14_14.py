def validate_numbers(numbers):
    expected_length = 7
    if len(numbers) != expected_length:
        raise ValueError(f"Expected {expected_length} numbers, got {len(numbers)}")
    
    for number in numbers:
        if not isinstance(number, float):
            raise TypeError("All elements must be floating-point numbers")

def sum_of_numbers():
    numbers = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7]
    validate_numbers(numbers)
    return sum(numbers)

if __name__ == '__main__':
    print(sum_of_numbers())