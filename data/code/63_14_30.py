def get_first_element(lst):
    if not isinstance(lst, list):
        raise ValueError('Input must be a list')
    if len(lst) == 0:
        return None
    return lst[0]

if __name__ == '__main__':
    sample_data = {
        'valid_list': [4, 5, 6],
        'empty_list': [],
        'invalid_input': "I am not a list"
    }
    
    for description, data in sample_data.items():
        try:
            result = get_first_element(data)
            print(f"{description}: {result}")
        except ValueError as e:
            print(f"{description}: {e}")