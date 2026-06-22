def get_element_at_index(lst, index):
    valid_index = 0 <= index < len(lst)
    return lst[index] if valid_index else None

if __name__ == '__main__':
    test_list = [100, 200, 300, 400, 500]
    indices_to_check = [2, 7, -2, 0]

    for idx in indices_to_check:
        element = get_element_at_index(test_list, idx)
        print(f"Element at index {idx}: {element}")