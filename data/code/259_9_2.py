def find_min_max(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    minimum = data[0]
    maximum = data[0]
    for x in data:
        if x < minimum:
            minimum = x
        if x > maximum:
            maximum = x
    return minimum, maximum
if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2, 8, 7, 6]
    min_val, max_val = find_min_max(sample_list)
    print(f"Minimum: {min_val}")
    print(f"Maximum: {max_val}")