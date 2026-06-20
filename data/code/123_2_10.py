import math

def validate_input(iterable):
    if not all(isinstance(x, float) for x in iterable):
        raise ValueError("All elements in the iterable must be floating-point numbers")

def sum_floats(iterable):
    validate_input(iterable)
    return math.fsum(iterable)

if __name__ == '__main__':
    sample_values = [0.1, 0.2, 0.3]
    total = sum_floats(sample_values)
    print(total)