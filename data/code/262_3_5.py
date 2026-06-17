def find_min_max(data):
    if not data:
        return None, None
    minimum = data[0]
    maximum = data[0]
    for x in data:
        if x < minimum:
            minimum = x
        if x > maximum:
            maximum = x
    return minimum, maximum
if __name__ == '__main__':
    sample_data = [3.14, 1.618, 2.718, 0.577, 9.81]
    minimum_val, maximum_val = find_min_max(sample_data)
    print(f"Minimum: {minimum_val}")
    print(f"Maximum: {maximum_val}")
    sample_data_2 = [-10.5, 5.2, -3.8, 100.0]
    minimum_val_2, maximum_val_2 = find_min_max(sample_data_2)
    print(f"Minimum: {minimum_val_2}")
    print(f"Maximum: {maximum_val_2}")
    empty_data = []
    minimum_val_3, maximum_val_3 = find_min_max(empty_data)
    print(f"Minimum: {minimum_val_3}")
    print(f"Maximum: {maximum_val_3}")