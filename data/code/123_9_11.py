from functools import reduce

def validate_input(numbers):
    if not isinstance(numbers, list) or not all(isinstance(x, (int, float)) for x in numbers):
        raise ValueError("Input must be a list of numbers")

def sum_numbers(numbers):
    validate_input(numbers)
    return reduce(lambda x, y: x + y, numbers)

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5]
    print(sum_numbers(sample_values))