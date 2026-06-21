def get_element_at_index(lst, index):
    if 0 <= index < len(lst):
        return lst[index]
    else:
        return None
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    print(get_element_at_index(sample_list, 2))
    print(get_element_at_index(sample_list, 5))
    print(get_element_at_index(sample_list, -1))