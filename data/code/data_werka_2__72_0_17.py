def compare_elements(list_one, list_two, target_index):
    sentinel = object()
    val_one = sentinel
    val_two = sentinel
    if 0 <= target_index < len(list_one):
        val_one = list_one[target_index]
    if 0 <= target_index < len(list_two):
        val_two = list_two[target_index]
    is_valid = val_one is not sentinel and val_two is not sentinel
    if is_valid:
        return val_one, val_two
    return None, None

if __name__ == '__main__':
    data_a = [1, 2, 3, 4, 5]
    data_b = [10, 20, 30, 40, 50]
    idx = 2
    out = compare_elements(data_a, data_b, idx)
    print(out)
    short_a = [1, 2]
    short_b = [10, 20, 30]
    bad_idx = 5
    out2 = compare_elements(short_a, short_b, bad_idx)
    print(out2)