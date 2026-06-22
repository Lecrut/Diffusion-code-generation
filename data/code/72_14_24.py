def validate_indices(indices, array_length):
    if not isinstance(indices, (list, tuple)):
        raise ValueError("Indices must be a list or tuple")
    for idx in indices:
        if not isinstance(idx, int):
            raise ValueError("All indices must be integers")
        if idx < 0:
            raise ValueError("Indices must be non-negative")
        if idx >= array_length:
            raise ValueError(f"Index {idx} out of bounds for array of length {array_length}")
    return True

def count_matching_at_positions(arr1, arr2, positions):
    min_len = min(len(arr1), len(arr2))
    validate_indices(positions, min_len)
    
    match_count = 0
    for pos in positions:
        if arr1[pos] == arr2[pos]:
            match_count += 1
    return match_count

if __name__ == '__main__':
    data_first = [5, 10, 15, 20, 25]
    data_second = [5, 12, 15, 22, 25]
    check_positions = [0, 1, 2, 3, 4]
    
    result = count_matching_at_positions(data_first, data_second, check_positions)
    print(result)