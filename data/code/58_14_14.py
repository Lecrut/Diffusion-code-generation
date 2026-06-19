def is_non_empty_list(lst):
    return isinstance(lst, list) and len(lst) > 0

def get_first_element(lst):
    if is_non_empty_list(lst):
        return lst[0]
    else:
        return None

if __name__ == '__main__':
    sample_values = [
        [1, 2, 3],
        [],
        ['apple', 'banana', 'cherry'],
        {'key': 'value'},
        42,
        None
    ]
    for i, value in enumerate(sample_values):
        print(f"First element of item {i+1}: {get_first_element(value)}")