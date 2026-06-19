def get_element_by_index(lst, index):
    if index < -len(lst) or index >= len(lst):
        raise IndexError('Index out of bounds')
    return lst[index]
if __name__ == '__main__':
    sample_list = [100, 200, 300, 400, 500]
    print(get_element_by_index(sample_list, 0))
    print(get_element_by_index(sample_list, -1))
    try:
        print(get_element_by_index(sample_list, 5))
    except IndexError as e:
        print(f'Error caught: {e}')
    try:
        print(get_element_by_index(sample_list, -6))
    except IndexError as e:
        print(f'Caught expected error: {e}')