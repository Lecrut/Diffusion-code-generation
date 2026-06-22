def validate_numbers(numbers):
    if not all(isinstance(num, int) and num > 0 for num in numbers):
        raise ValueError("All elements must be positive integers")

def cycle_and_double(numbers):
    for number in numbers:
        print(number * 2)

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    validate_numbers(sample_values)
    cycle_and_double(sample_values)