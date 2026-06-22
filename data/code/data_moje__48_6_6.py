import operator
import functools

def find_max(values):
    if not values:
        raise ValueError("Sequence cannot be empty")
    return functools.reduce(operator.max, values)

if __name__ == '__main__':
    sample_data = [34, 7, 19, 92, 45, 12, 88]
    result = find_max(sample_data)
    print(result)