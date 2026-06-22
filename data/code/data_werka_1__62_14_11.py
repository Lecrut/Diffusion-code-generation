def get_second_item(lst):
    if len(lst) < 2:
        return None
    return lst[1]
if __name__ == '__main__':
    sample_list_1 = [10, 20, 30, 40]
    sample_list_2 = [5, 15]
    sample_list_3 = [7]
    sample_list_4 = []
    print(get_second_item(sample_list_1))
    print(get_second_item(sample_list_2))
    print(get_second_item(sample_list_3))
    print(get_second_item(sample_list_4))