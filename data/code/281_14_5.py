def validate_numbers(numbers):
    if not isinstance(numbers, list) or len(numbers) != 7:
        raise ValueError("Input must be a list of exactly seven numbers.")
    for num in numbers:
        if not isinstance(num, (int, float)):
            raise TypeError("All elements must be integers or floats.")

def sum_of_numbers():
    numbers = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7]
    validate_numbers(numbers)
    return sum(numbers)

if __name__ == '__main__':
    print(sum_of_numbers())