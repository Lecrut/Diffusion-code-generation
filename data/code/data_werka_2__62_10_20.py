def get_second_item(lst):
    try:
        return lst[1]
    except IndexError:
        return None
if __name__ == '__main__':
    sample_list_1 = [1, 2, 3]
    sample_list_2 = [42]
    sample_list_3 = []
    print(get_second_item(sample_list_1))
    print(get_second_item(sample_list_2))
    print(get_second_item(sample_list_3))