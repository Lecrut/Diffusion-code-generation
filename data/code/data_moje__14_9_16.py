def get_third_element(lst, default=None):
    if len(lst) > 2:
        return lst[2]
    return default

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    short_list = [1, 2]
    empty_list = []

    result1 = get_third_element(sample_list, default='N/A')
    result2 = get_third_element(short_list, default='N/A')
    result3 = get_third_element(empty_list, default='N/A')

    print(result1)
    print(result2)
    print(result3)