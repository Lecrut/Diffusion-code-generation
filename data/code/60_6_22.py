def get_last_element(lst):
    if not isinstance(lst, list):
        raise TypeError("Input must be a list")
    try:
        return lst[-1]
    except IndexError:
        return None

if __name__ == '__main__':
    sample_data = {
        'list1': [1, 2, 3, 4, 5],
        'list2': [],
        'list3': ['a', 'b', 'c'],
        'list4': [True, False]
    }

    for key, value in sample_data.items():
        print(f"Last element of {key}: {get_last_element(value)}")