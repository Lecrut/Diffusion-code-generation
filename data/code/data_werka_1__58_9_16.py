def get_first_element(lst):
    return lst[0] if lst else None
if __name__ == '__main__':
    sample_list = [42, 84, 168]
    empty_list = []
    print(get_first_element(sample_list))
    print(get_first_element(empty_list))