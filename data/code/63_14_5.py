def get_first_element(lst):
    if not isinstance(lst, list):
        raise TypeError('Input must be a list')
    return lst[0] if lst else None

if __name__ == '__main__':
    sample_lists = [
        [42, 84, 168],
        [],
        ['hello', 'world'],
        [True, False, True],
        [None, 'not None']
    ]
    
    for idx, sample_list in enumerate(sample_lists):
        print(f"First element of list {idx + 1}: {get_first_element(sample_list)}")