from functools import reduce

def min_value(numbers):
    if not numbers:
        raise ValueError("The list cannot be empty")
    return reduce(lambda x, y: x if x < y else y, numbers)

if __name__ == '__main__':
    sample_values = [4, 7, 1, 3, 9]
    try:
        print(min_value(sample_values))
    except ValueError as e:
        print(e)