def check_item_existence(item_list, item):
    set_list = set(item_list)
    return item in set_list
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    sample_item = 3
    print(check_item_existence(sample_list, sample_item))
    sample_item = 6
    print(check_item_existence(sample_list, sample_item))