def get_element_at_index(lst, index):
    if not isinstance(index, int):
        raise ValueError("Index must be an integer")
    if index < 0 or index >= len(lst):
        raise IndexError("Index out of bounds")
    return lst[index]

if __name__ == '__main__':
    sample_list = [7, 14, 21, 28, 35]
    try:
        element = get_element_at_index(sample_list, 3)
        print(element)
    except (ValueError, IndexError) as e:
        print(e)