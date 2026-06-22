def is_valid_index(lst, index):
    return 0 <= index < len(lst)

def get_element_at_index(lst, index):
    if not isinstance(index, int):
        raise ValueError("Index must be an integer")
    if not is_valid_index(lst, index):
        raise IndexError("Index out of bounds")
    return lst[index]

if __name__ == '__main__':
    sample_list = [10000, 20000, 30000, 40000, 50000]
    index_to_find = 4
    try:
        element = get_element_at_index(sample_list, index_to_find)
        print(element)
    except (ValueError, IndexError) as e:
        print(e)