def get_element_at_index(lst, index):
    if not isinstance(index, int):
        raise ValueError("Index must be an integer")
    try:
        return lst[index]
    except IndexError:
        return None

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    index_to_find = 2
    element = get_element_at_index(sample_list, index_to_find)
    if element is not None:
        print(f"Element at index {index_to_find}: {element}")
    else:
        print("Index out of bounds")