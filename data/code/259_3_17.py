def initialize_min_max(values):
    if not values:
        raise ValueError("Input list cannot be empty")
    return float('inf'), float('-inf')

def update_min_max(min_val, max_val, value):
    if value < min_val:
        min_val = value
    if value > max_val:
        max_val = value
    return min_val, max_val

def find_min_max(values):
    min_val, max_val = initialize_min_max(values)
    for value in values:
        min_val, max_val = update_min_max(min_val, max_val, value)
    return min_val, max_val

if __name__ == '__main__':
    sample_values = [3.141592653589793, 2.718281828459045, 1.4142135623730951, 0.5772156649015328]
    try:
        min_val, max_val = find_min_max(sample_values)
        print(f"Minimum: {min_val}, Maximum: {max_val}")
    except ValueError as e:
        print(e)