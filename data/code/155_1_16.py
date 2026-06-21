from functools import reduce

def validate_input(iterable):
    if not isinstance(iterable, (list, tuple)):
        raise ValueError("Input must be a list or tuple")
    if not all(isinstance(item, (int, float)) for item in iterable):
        raise ValueError("All elements in the input must be numbers")

def compute_total(numbers):
    validate_input(numbers)
    return reduce(lambda x, y: x + y, numbers)

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5]
    print(f"Total of {sample_numbers}: {compute_total(sample_numbers)}")