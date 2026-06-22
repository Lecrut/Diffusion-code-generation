def safe_last_element(lst):
    if not isinstance(lst, list):
        raise TypeError("Input must be a list")
    if len(lst) == 0:
        return None
    return lst[-1]

if __name__ == '__main__':
    sample_data = {
        'data1': [1, 2, 3, 4, 5],
        'data2': [],
        'data3': ['a', 'b', 'c'],
        'data4': [True, False, True]
    }
    
    for key, value in sample_data.items():
        print(f"Last element of {key}: {safe_last_element(value)}")