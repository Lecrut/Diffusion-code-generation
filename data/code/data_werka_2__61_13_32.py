def is_valid_index(lst, index):
    return 0 <= index < len(lst)

def get_element_at_index(lst, index):
    if is_valid_index(lst, index):
        return lst[index]
    else:
        return None

if __name__ == '__main__':
    sample_list = [100, 200, 300, 400, 500]
    indices_to_test = [2, 6, -1, 0]
    for idx in indices_to_test:
        print(get_element_at_index(sample_list, idx))