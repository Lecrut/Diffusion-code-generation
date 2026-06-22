def is_first_le_second_at(lst_first, lst_second, idx):
    if idx < 0:
        raise ValueError("Index cannot be negative")
    if idx >= len(lst_first):
        raise ValueError("Index out of range for first list")
    if idx >= len(lst_second):
        raise ValueError("Index out of range for second list")
    first_val = lst_first[idx]
    second_val = lst_second[idx]
    return first_val <= second_val

if __name__ == '__main__':
    list_one = [1, 3, 5, 7]
    list_two = [2, 2, 6, 8]
    target_idx = 2
    comparison_result = is_first_le_second_at(list_one, list_two, target_idx)
    print(comparison_result)