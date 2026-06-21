def remove_last_element(lst):
    if lst:
        lst.pop(-1)
    return lst
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4]
    print(remove_last_element(sample_list))
    empty_list = []
    print(remove_last_element(empty_list))