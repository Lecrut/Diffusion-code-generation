def get_second_item(lst):
    if len(lst) < 2:
        return None
    return lst[1]
if __name__ == '__main__':
    sample_list_1 = [1, 2, 3, 4]
    sample_list_2 = [5]
    sample_list_3 = []
    print(get_second_item(sample_list_1))
    print(get_second_item(sample_list_2))
    print(get_second_item(sample_list_3))