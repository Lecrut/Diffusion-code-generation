def validate_index(lst, index):
    if not isinstance(index, int):
        raise TypeError('Index must be an integer.')
    if index < 0 or index >= len(lst):
        raise IndexError('Index out of bounds.')

def get_element_by_position(lst, index):
    validate_index(lst, index)
    return lst[index]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    try:
        print(get_element_by_position(sample_list, 2))
    except IndexError as e:
        print(e)

    try:
        print(get_element_by_position(sample_list, -1))
    except IndexError as e:
        print(e)

    try:
        print(get_element_by_position(sample_list, 5))
    except IndexError as e:
        print(e)