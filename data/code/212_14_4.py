def find_min_max(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    minimum = data[0]
    maximum = data[0]
    for x in data[1:]:
        if x < minimum:
            minimum = x
        if x > maximum:
            maximum = x
    return minimum, maximum
if __name__ == '__main__':
    sample_list = [3.14, 1.618, 2.718, -0.5, 99.9, -100.0, 5.0]
    min_val, max_val = find_min_max(sample_list)
    print(f"Sample List: {sample_list}")
    print(f"Minimum element: {min_val}")
    print(f"Maximum element: {max_val}")