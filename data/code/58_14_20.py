def get_first_element(lst):
    if not lst:
        return None
    first_element = lst[0]
    return first_element

if __name__ == '__main__':
    sample_values = [
        [7, 14, 21],
        [],
        ['cat', 'dog', 'bird'],
        [True, False, True, False]
    ]
    for i, value in enumerate(sample_values):
        print(f"First element of list {i+1}: {get_first_element(value)}")