def get_first_element(lst):
    if lst:
        return lst[0]
    else:
        return None
if __name__ == '__main__':
    sample_list = [42, 3.14, 'hello']
    print(get_first_element(sample_list))
    empty_list = []
    print(get_first_element(empty_list))