def get_element_at_index(lst, index):
    return lst[index] if 0 <= index < len(lst) else None

if __name__ == '__main__':
    sample_list = [5, 15, 25, 35, 45]
    indices_to_test = [2, 5, -1, 0]
    for idx in indices_to_test:
        print(get_element_at_index(sample_list, idx))