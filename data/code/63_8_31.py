def get_first_element(lst):
    if not lst:
        raise ValueError("The input list is empty")
    return lst[0]

if __name__ == '__main__':
    sample_values = [
        [1, 2, 3],
        [],
        ['a', 'b', 'c'],
        [42],
        [3.14, 2.71]
    ]
    
    for value in sample_values:
        try:
            print(get_first_element(value))
        except ValueError as e:
            print(e)