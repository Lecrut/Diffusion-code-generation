def validate_input(lst):
    if not isinstance(lst, list):
        raise TypeError('Input must be a list')

def get_first_element(lst):
    validate_input(lst)
    if len(lst) == 0:
        return None
    return lst[0]

if __name__ == '__main__':
    sample_data = [
        [10, 20, 30],
        [],
        ['x', 'y', 'z'],
        [True, False],
        [None]
    ]
    for data in sample_data:
        print(get_first_element(data))