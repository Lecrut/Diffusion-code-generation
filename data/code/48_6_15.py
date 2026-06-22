import operator

def find_max(values):
    if not values:
        raise ValueError("Values list cannot be empty")
    current_max = values[0]
    for value in values:
        if operator.gt(value, current_max):
            current_max = value
    return current_max

if __name__ == '__main__':
    sample_values = [10, 45, 2, 89, 33, 67, 12, 99]
    result = find_max(sample_values)
    print(result)