from functools import reduce

def validate_input(numbers):
    if not isinstance(numbers, list) or not all(isinstance(x, (int, float)) for x in numbers):
        raise ValueError("Input must be a list of numbers")

def find_max(numbers):
    validate_input(numbers)
    return reduce(lambda x, y: x if x > y else y, numbers)

if __name__ == '__main__':
    sample_numbers = [3, 5, 1, 2, 4]
    print(find_max(sample_numbers))