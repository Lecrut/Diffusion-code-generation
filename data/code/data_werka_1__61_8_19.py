def get_element_at_index(lst, index):
    if 0 <= index < len(lst):
        return lst[index]
    else:
        raise IndexError("Index out of range")

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    index_to_find = 3
    try:
        element = get_element_at_index(sample_list, index_to_find)
        print(element)
    except IndexError as e:
        print(e)