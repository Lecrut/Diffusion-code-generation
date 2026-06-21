def find_first_element(lst):
    if not isinstance(lst, list):
        raise ValueError('Input must be a list')
    if len(lst) == 0:
        return None
    return lst[0]
if __name__ == '__main__':
    sample_list = [1, 2, 3]
    print(find_first_element(sample_list))
    empty_list = []
    print(find_first_element(empty_list))
    non_list_input = 'not a list'
    try:
        print(find_first_element(non_list_input))
    except ValueError as e:
        print(e)