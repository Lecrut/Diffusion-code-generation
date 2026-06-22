def get_first_element(lst):
    if not isinstance(lst, list):
        raise TypeError('Input must be a list')
    return lst[0] if lst else None

if __name__ == '__main__':
    sample_data = [
        [42, 84, 168],
        [],
        ['hello', 'world'],
        [3.14, 2.71],
        [True]
    ]
    for data in sample_data:
        print(get_first_element(data))