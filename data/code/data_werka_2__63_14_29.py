def validate_input(lst):
    if not isinstance(lst, list):
        raise ValueError('Input must be a list')

def get_first_element(lst):
    validate_input(lst)
    if len(lst) == 0:
        return None
    return lst[0]

if __name__ == '__main__':
    sample_list = [4, 5, 6]
    empty_list = []
    non_list_input = 'not a list'
    
    try:
        print(get_first_element(sample_list))
    except ValueError as e:
        print(e)
    
    try:
        print(get_first_element(empty_list))
    except ValueError as e:
        print(e)
    
    try:
        print(get_first_element(non_list_input))
    except ValueError as e:
        print(e)