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
    sample_list = [15, 3, 88, 42, 9, 71]
    min_val, max_val = find_min_max(sample_list)
    print(f"Data: {sample_list}")
    print(f"Minimum: {min_val}")
    print(f"Maximum: {max_val}")
    sample_tuple = (100, 50, 200, 10, 150)
    min_val_t, max_val_t = find_min_max(sample_tuple)
    print(f"\nData: {sample_tuple}")
    print(f"Minimum: {min_val_t}")
    print(f"Maximum: {max_val_t}")
    empty_list = []
    min_val_e, max_val_e = find_min_max(empty_list)
    print(f"\nData: {empty_list}")
    print(f"Minimum: {min_val_e}")
    print(f"Maximum: {max_val_e}")