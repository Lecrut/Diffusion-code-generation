def find_min_max(data):
    if not data:
        return None, None
    minimum = maximum = data[0]
    for value in data[1:]:
        if value < minimum:
            minimum = value
        elif value > maximum:
            maximum = value
    return minimum, maximum

if __name__ == '__main__':
    sample_list = [3.14, 1.618, 2.718, -0.5, 100.0, -50.2]
    minimum_val, maximum_val = find_min_max(sample_list)
    print(f"Minimum: {minimum_val}")
    print(f"Maximum: {maximum_val}")