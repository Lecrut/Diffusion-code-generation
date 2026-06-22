def is_valid_list(input_data):
    return isinstance(input_data, list)

def get_first_element(lst):
    if not is_valid_list(lst):
        raise ValueError("Input must be a list")
    if len(lst) == 0:
        return None
    return lst[0]

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