def unique_common_items(list1, list2):
    common_items = []
    for item in list1:
        if item not in common_items and item in list2:
            common_items.append(item)
    return common_items

if __name__ == '__main__':
    sample_list1 = [10, 20, 30, 40, 50]
    sample_list2 = [40, 50, 60, 70, 80]
    print(unique_common_items(sample_list1, sample_list2))