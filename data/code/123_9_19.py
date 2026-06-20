from functools import reduce

def validate_numbers(numbers):
    if not isinstance(numbers, list) or not all(isinstance(n, (int, float)) for n in numbers):
        raise ValueError("Input must be a list of numbers")

def sum_numbers(numbers):
    validate_numbers(numbers)
    return reduce(lambda x, y: x + y, numbers)

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5]
    total_sum = sum_numbers(sample_values)
    print(total_sum)