def find_min_max(data):
    if not data:
        return None, None
    return min(data), max(data)

if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2, 8]
    min_val, max_val = find_min_max(sample_list)
    print(f"Minimum: {min_val}")
    print(f"Maximum: {max_val}")

    sample_list_empty = []
    min_val_empty, max_val_empty = find_min_max(sample_list_empty)
    print(f"Empty list Min: {min_val_empty}, Max: {max_val_empty}")