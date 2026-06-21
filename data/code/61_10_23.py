def get_element_at_position(lst, index):
    if not isinstance(lst, list):
        raise TypeError('The first argument must be a list.')
    if not isinstance(index, int):
        raise TypeError('The second argument must be an integer.')
    if index < 0 or index >= len(lst):
        raise ValueError('Index is out of bounds.')
    return lst[index]
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    try:
        print(get_element_at_position(sample_list, 2))
        print(get_element_at_position(sample_list, 5))
    except ValueError as e:
        print(e)