def extract_pair_at_index(source_a, source_b, target_index):
    if not isinstance(source_a, list) or not isinstance(source_b, list):
        raise ValueError("Inputs must be lists")
    if not isinstance(target_index, int):
        raise ValueError("Index must be an integer")
    if target_index < 0 or target_index >= len(source_a):
        raise ValueError("Index out of range for first list")
    if target_index < 0 or target_index >= len(source_b):
        raise ValueError("Index out of range for second list")
    val_a = source_a[target_index]
    val_b = source_b[target_index]
    return [(val_a, val_b)]

if __name__ == '__main__':
    data_x = [100, 200, 300]
    data_y = [400, 500, 600]
    position = 2
    extracted = extract_pair_at_index(data_x, data_y, position)
    print(extracted)