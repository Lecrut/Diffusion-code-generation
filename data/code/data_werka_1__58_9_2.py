def get_first_element(lst):
    if not lst:
        return None
    return lst[0]
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    empty_list = []
    print(get_first_element(sample_list))
    print(get_first_element(empty_list))