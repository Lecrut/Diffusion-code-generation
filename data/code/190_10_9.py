def contains_item(target_list: list, item_to_find: any) -> bool:
    return item_to_find in set(target_list)
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    item_to_check = 5
    print(contains_item(sample_list, item_to_check))