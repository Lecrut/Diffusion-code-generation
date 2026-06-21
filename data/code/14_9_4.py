def get_third_element(lst, default=None):
    if len(lst) > 2:
        return lst[2]
    return default

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(get_third_element(sample_list))
    short_list = [1, 2]
    print(get_third_element(short_list, default="N/A"))
    empty_list = []
    print(get_third_element(empty_list, default="Empty"))