def get_first_element(lst):
    if not isinstance(lst, list):
        raise TypeError('Input must be a list')
    if len(lst) == 0:
        return None
    return lst[0]
if __name__ == '__main__':
    sample_list_1 = [1, 2, 3]
    sample_list_2 = []
    sample_list_3 = ['a', 'b', 'c']
    print(get_first_element(sample_list_1))
    print(get_first_element(sample_list_2))
    print(get_first_element(sample_list_3))