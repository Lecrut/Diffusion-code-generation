def get_first_element(lst):
    if not isinstance(lst, list):
        raise TypeError("Input must be a list")
    try:
        return lst[0]
    except IndexError:
        return None

if __name__ == '__main__':
    sample_data = [
        [10, 20, 30],
        [],
        ['x', 'y', 'z'],
        [True, False],
        [None, 'value']
    ]
    for data in sample_data:
        print(get_first_element(data))