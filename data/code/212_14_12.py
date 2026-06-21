def find_min_max(data):
    if not data:
        return None, None
    minimum = data[0]
    maximum = data[0]
    for value in data[1:]:
        if value < minimum:
            minimum = value
        if value > maximum:
            maximum = value
    return minimum, maximum

if __name__ == '__main__':
    sample_list = [5.772, 3.14, 6.283, -2.0, 99.9, -100.0]
    min_val, max_val = find_min_max(sample_list)
    print(f"Minimum: {min_val}")
    print(f"Maximum: {max_val}")