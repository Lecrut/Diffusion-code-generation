def get_element_by_position(lst, index):
    try:
        return lst[index]
    except IndexError:
        raise IndexError("Index out of bounds")

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    index_to_access = 3
    print(get_element_by_position(sample_list, index_to_access))