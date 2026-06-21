def validate_data(data):
    if not data:
        raise ValueError("Input list must not be empty")
    if not all(isinstance(x, (int, float)) for x in data):
        raise TypeError("All elements in the input list must be numbers")

def find_min_max(data):
    validate_data(data)
    minimum = maximum = data[0]
    for x in data[1:]:
        if x < minimum:
            minimum = x
        if x > maximum:
            maximum = x
    return minimum, maximum

if __name__ == '__main__':
    sample_list = [3.14, 1.618, 2.718, -0.5, 100.0, -50.2]
    try:
        minimum_val, maximum_val = find_min_max(sample_list)
        print(f"Minimum: {minimum_val}")
        print(f"Maximum: {maximum_val}")
    except (ValueError, TypeError) as e:
        print(e)