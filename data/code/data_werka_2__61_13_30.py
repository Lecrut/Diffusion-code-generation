def get_element_at_index(lst, index):
    try:
        return lst[index]
    except IndexError:
        return None

if __name__ == '__main__':
    sample_list = [100, 200, 300, 400, 500]
    indices_to_test = [2, 7, -2, 0, 4]
    for idx in indices_to_test:
        print(get_element_at_index(sample_list, idx))