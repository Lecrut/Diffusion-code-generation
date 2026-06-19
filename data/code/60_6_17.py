def get_last_element(lst):
    if not isinstance(lst, list):
        raise TypeError('Input must be a list')
    if len(lst) == 0:
        return None
    last_item = lst[-1]
    return last_item
if __name__ == '__main__':
    sample_list_1 = [1, 2, 3, 4, 5]
    sample_list_2 = []
    sample_list_3 = ['a', 'b', 'c']
    print(get_last_element(sample_list_1))
    print(get_last_element(sample_list_2))
    print(get_last_element(sample_list_3))