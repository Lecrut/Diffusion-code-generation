def validate_indices(indices, length):
    if not isinstance(indices, (list, tuple)):
        raise ValueError("Indices must be a list or tuple")
    for idx in indices:
        if not isinstance(idx, int):
            raise ValueError("Each index must be an integer")
        if idx < 0 or idx >= length:
            raise ValueError(f"Index {idx} out of bounds for length {length}")

def count_matching_values(arr1, arr2, indices):
    validate_indices(indices, len(arr1))
    validate_indices(indices, len(arr2))
    count = 0
    for i in indices:
        if arr1[i] == arr2[i]:
            count += 1
    return count

if __name__ == '__main__':
    array_x = [5, 10, 15, 20, 25]
    array_y = [5, 12, 15, 22, 25]
    check_positions = [0, 1, 2, 3, 4]
    match_count = count_matching_values(array_x, array_y, check_positions)
    print(match_count)