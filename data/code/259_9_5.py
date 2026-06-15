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
    sample_list = [3, 1, 4, 1, 5, 9, 2, 8]
    min_val, max_val = find_min_max(sample_list)
    print(f"Minimum: {min_val}")
    print(f"Maximum: {max_val}")
    sample_list_2 = [-10, 5, 0, -20, 100]
    min_val_2, max_val_2 = find_min_max(sample_list_2)
    print(f"Minimum: {min_val_2}")
    print(f"Maximum: {max_val_2}")
    sample_list_3 = [7]
    min_val_3, max_val_3 = find_min_max(sample_list_3)
    print(f"Minimum: {min_val_3}")
    print(f"Maximum: {max_val_3}")