def get_element_at_index(lst, index):
    if not (0 <= index < len(lst)):
        return None
    return lst[index]

if __name__ == '__main__':
    sample_list = [100, 200, 300, 400, 500]
    indices_to_test = [1, 4, 6, -2]
    for idx in indices_to_test:
        print(get_element_at_index(sample_list, idx))