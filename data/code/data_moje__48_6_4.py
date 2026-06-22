import operator
import functools

def find_max(*values):
    if not values:
        raise ValueError("At least one value is required")
    return functools.reduce(operator.max, values)

if __name__ == '__main__':
    sample_values = [3, 5, 2, 9, 1, 7, 4]
    result = find_max(*sample_values)
    print(result)