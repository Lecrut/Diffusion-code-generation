def find_min_max(data):
    if not data:
        raise ValueError("Input iterable cannot be empty")
    minimum = data[0]
    maximum = data[0]
    for x in data:
        if x < minimum:
            minimum = x
        if x > maximum:
            maximum = x
    return minimum, maximum
if __name__ == '__main__':
    sample_data = [3.14, 1.618, 2.718, -0.5, 10.0, -2.3]
    min_val, max_val = find_min_max(sample_data)
    print(f"Minimum: {min_val}")
    print(f"Maximum: {max_val}")