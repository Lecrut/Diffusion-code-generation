def contains_item(item_list: list, target: any) -> bool:
    item_set = set(item_list)
    return target in item_set

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target_item = 5
    print(contains_item(sample_list, target_item))