def validate_numbers(numbers):
    if not isinstance(numbers, list) or not all(isinstance(x, int) for x in numbers):
        raise ValueError("Input must be a list of integers")

def calculate_total_sum(numbers):
    validate_numbers(numbers)
    return sum(numbers)

if __name__ == '__main__':
    sample_numbers = [10, 25, 5, 42, 18]
    total_sum = calculate_total_sum(sample_numbers)
    print(total_sum)