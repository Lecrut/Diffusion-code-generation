def get_element_at_index(lst, index):
    return lst[index]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    index_to_find = 2
    element = get_element_at_index(sample_list, index_to_find)
    print(element)