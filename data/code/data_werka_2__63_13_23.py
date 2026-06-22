def get_first_element(lst):
    if not isinstance(lst, list):
        raise ValueError("Input must be a list")
    return lst[0] if lst else None

if __name__ == '__main__':
    sample_data = [
        [1, 2, 3],
        [],
        ['a', 'b', 'c'],
        [True, False],
        [None]
    ]
    for data in sample_data:
        print(get_first_element(data))