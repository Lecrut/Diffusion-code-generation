def get_element_at_position(lst, position):
    if not isinstance(position, int):
        raise TypeError('Position must be an integer.')
    if position < 0 or position >= len(lst):
        raise IndexError('Position out of range.')
    return lst[position]
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    try:
        print(get_element_at_position(sample_list, 2))
        print(get_element_at_position(sample_list, -1))
    except (TypeError, IndexError) as e:
        print(e)