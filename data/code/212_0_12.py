def find_min_max(data):
    if not data:
        return None, None
    return min(data), max(data)

if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2, 8]
    print(f"Minimum: {find_min_max(sample_list)[0]}")
    print(f"Maximum: {find_min_max(sample_list)[1]}")

    sample_list_empty = []
    min_val_empty, max_val_empty = find_min_max(sample_list_empty)
    print(f"Empty list Min: {min_val_empty}, Max: {max_val_empty}")