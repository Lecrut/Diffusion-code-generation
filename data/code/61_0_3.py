def get_element_at_index(lst, index):
    try:
        return lst[index]
    except IndexError:
        return None
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    index_to_retrieve = 3
    element = get_element_at_index(sample_list, index_to_retrieve)
    print(element)
    index_to_retrieve = 10
    element = get_element_at_index(sample_list, index_to_retrieve)
    print(element)