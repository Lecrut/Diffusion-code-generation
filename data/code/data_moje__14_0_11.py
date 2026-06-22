def get_third_element(lst):
    if len(lst) < 3:
        raise IndexError("List has fewer than three items")
    return lst[2]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    print(get_third_element(sample_list))
    short_list = [1, 2]
    print(get_third_element(short_list))