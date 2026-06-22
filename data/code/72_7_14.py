def _validate_index_access(data_a, data_b, idx):
    n_a = len(data_a)
    n_b = len(data_b)
    if idx < 0:
        raise ValueError("Negative index provided")
    if idx >= n_a:
        raise ValueError("Index out of bounds for first list")
    if idx >= n_b:
        raise ValueError("Index out of bounds for second list")
    return data_a[idx], data_b[idx]

def is_first_at_index_le(list_a, list_b, index):
    val_first, val_second = _validate_index_access(list_a, list_b, index)
    return val_first <= val_second

if __name__ == '__main__':
    first_list = [1, 3, 5, 7]
    second_list = [1, 2, 6, 8]
    target_idx = 2
    answer = is_first_at_index_le(first_list, second_list, target_idx)
    print(answer)