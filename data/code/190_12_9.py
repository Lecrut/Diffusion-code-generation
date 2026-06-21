def check_item_existence(item_list, item):
    return item in set(item_list)

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    test_items = [3, 6]
    for item in test_items:
        print(check_item_existence(sample_list, item))