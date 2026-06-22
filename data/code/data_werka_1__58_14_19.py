def get_first_element(lst):
    DEFAULT_VALUE = None
    return lst[0] if lst else DEFAULT_VALUE

if __name__ == '__main__':
    SAMPLE_LISTS = [
        [1, 2, 3],
        [],
        ['apple', 'banana', 'cherry'],
        [True, False, True],
        [42, 84, 168]
    ]
    
    for i, lst in enumerate(SAMPLE_LISTS):
        print(f"First element of list {i+1}: {get_first_element(lst)}")