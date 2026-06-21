def get_first_element(lst):
    if not isinstance(lst, list):
        raise TypeError("Input must be a list")
    first_element = None if len(lst) == 0 else lst[0]
    return first_element

if __name__ == '__main__':
    sample_data = [
        [10, 20, 30],
        [],
        ['x', 'y', 'z'],
        [True, False, True],
        [None, None]
    ]
    for idx, data in enumerate(sample_data):
        result = get_first_element(data)
        print(f"Sample {idx + 1}: First element is {result}")