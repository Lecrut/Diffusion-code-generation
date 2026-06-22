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
        ['a', 'b', 'c'],
        [True, False],
        42,
        "string",
        None
    ]
    
    for value in sample_values:
        print(f"First element of {value}: {get_first_element(value)}")