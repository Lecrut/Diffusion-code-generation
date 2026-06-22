def get_second_item(lst):
    if len(lst) < 2:
        return None
    return lst[1]
if __name__ == '__main__':
    sample_list_1 = [10, 20, 30, 40, 50]
    sample_list_2 = [5]
    print(get_second_item(sample_list_1))
    print(get_second_item(sample_list_2))