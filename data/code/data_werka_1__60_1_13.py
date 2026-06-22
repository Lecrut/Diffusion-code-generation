def get_last_item(data):
    if not isinstance(data, list):
        raise TypeError('Input must be a list')
    if not data:
        return None
    return data[-1]
if __name__ == '__main__':
    sample_list_1 = [10, 20, 30, 40, 50]
    sample_list_2 = ['x', 'y', 'z']
    empty_list = []
    single_element_list = [42]
    print(get_last_item(sample_list_1))
    print(get_last_item(sample_list_2))
    print(get_last_item(empty_list))
    print(get_last_item(single_element_list))
    try:
        get_last_item('not a list')
    except TypeError as e:
        print(f'Error for non-list input: {e}')