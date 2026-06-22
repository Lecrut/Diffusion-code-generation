def validate_index(lst, index):
    if not isinstance(index, int):
        raise ValueError("Index must be an integer")
    if index < 0 or index >= len(lst):
        raise IndexError("Index out of bounds")

def get_element_at_index(lst, index):
    validate_index(lst, index)
    return lst[index]

if __name__ == '__main__':
    sample_list = [50, 60, 70, 80, 90]
    index_to_find = 3
    try:
        element = get_element_at_index(sample_list, index_to_find)
        print(element)
    except (ValueError, IndexError) as e:
        print(e)