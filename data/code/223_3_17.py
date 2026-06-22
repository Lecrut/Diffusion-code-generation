from functools import reduce

def validate_numbers(numbers):
    if not numbers:
        raise ValueError("The list cannot be empty")
    if not all(isinstance(x, (int, float)) for x in numbers):
        raise TypeError("All elements must be numbers")

def find_max(numbers):
    validate_numbers(numbers)
    return reduce(lambda x, y: x if x > y else y, numbers)

if __name__ == '__main__':
    sample_numbers = [3, 5, 1, 2, 4]
    print(find_max(sample_numbers))