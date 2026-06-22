def get_element_by_index(lst, index):
    MAX_INDEX = len(lst) - 1
    MIN_INDEX = -len(lst)
    if index < MIN_INDEX or index > MAX_INDEX:
        raise IndexError('Index out of bounds')
    return lst[index]
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    print(get_element_by_index(sample_list, 0))
    print(get_element_by_index(sample_list, -1))
    try:
        print(get_element_by_index(sample_list, 5))
    except IndexError as e:
        print(e)
    try:
        print(get_element_by_index(sample_list, -6))
    except IndexError as e:
        print(e)