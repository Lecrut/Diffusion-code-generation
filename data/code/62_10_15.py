def get_second_item(lst):
    return lst[1] if len(lst) > 1 else None
if __name__ == '__main__':
    sample_list_1 = [1, 2, 3]
    sample_list_2 = ['a']
    sample_list_3 = []
    print(get_second_item(sample_list_1))
    print(get_second_item(sample_list_2))
    print(get_second_item(sample_list_3))