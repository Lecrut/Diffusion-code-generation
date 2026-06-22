def get_last_element(lst):
    if not lst:
        raise ValueError("The list is empty")
    return lst[-1]

if __name__ == '__main__':
    sample_lists = {
        'list_1': [1, 2, 3, 4, 5],
        'list_2': [],
        'list_3': ['a', 'b', 'c'],
        'list_4': [True, False, True]
    }

    for name, lst in sample_lists.items():
        try:
            print(f"Last element of {name}: {get_last_element(lst)}")
        except ValueError as e:
            print(f"Error for {name}: {e}")