def unique_common_items(list1, list2):
    item_count = {}
    for item in list1:
        if item not in item_count:
            item_count[item] = 0
    common_items = []
    for item in list2:
        if item in item_count and item not in common_items:
            common_items.append(item)
    return common_items

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5]
    sample_list2 = [4, 5, 6, 7, 8]
    print(unique_common_items(sample_list1, sample_list2))