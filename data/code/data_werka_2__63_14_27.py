def get_first_element(lst):
    if not isinstance(lst, list):
        raise ValueError('Input must be a list')
    try:
        return lst[0]
    except IndexError:
        return None

if __name__ == '__main__':
    sample_list = [42, 84, 168]
    empty_list = []
    non_list_input = "This is not a list"
    
    test_cases = [
        (sample_list, 'Sample List'),
        (empty_list, 'Empty List'),
        (non_list_input, 'Non-List Input')
    ]
    
    for value, description in test_cases:
        try:
            print(f"{description}: {get_first_element(value)}")
        except ValueError as e:
            print(f"{description}: {e}")