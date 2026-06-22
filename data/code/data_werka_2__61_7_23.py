def get_element_at_index(lst, index):
    return lst[index] if 0 <= index < len(lst) else None

if __name__ == '__main__':
    sample_list = [100, 200, 300, 400, 500]
    index_to_find = 3
    element = get_element_at_index(sample_list, index_to_find)
    if element is not None:
        print(element)
    else:
        print("Index out of bounds")