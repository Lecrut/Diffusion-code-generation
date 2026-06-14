def find_min_max(data):
    if not data:
        return None, None
    minimum = data[0]
    maximum = data[0]
    for element in data:
        if element < minimum:
            minimum = element
        if element > maximum:
            maximum = element
    return minimum, maximum
if __name__ == '__main__':
    sample_list = [3.14, 1.618, 2.718, -0.5, 10.0, -3.14159, 0.0]
    minimum_val, maximum_val = find_min_max(sample_list)
    print(f"Minimum: {minimum_val}")
    print(f"Maximum: {maximum_val}")