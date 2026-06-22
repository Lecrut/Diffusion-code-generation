def get_element_at_index(lst, index):
    if index < 0 or index >= len(lst):
        raise IndexError("Index out of bounds")
    return lst[index]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    index_to_find = 2
    try:
        element = get_element_at_index(sample_list, index_to_find)
        print(element)
    except IndexError as e:
        print(e)