def merge_store_dicts(list1, list2):
    dict2_map = {store['name']: store for store in list2}
    merged_list = []
    for store in list1:
        if store['name'] in dict2_map:
            merged_list.append(dict2_map[store['name']])
        else:
            merged_list.append(store)
    return merged_list

if __name__ == '__main__':
    sample_list1 = [{'name': 'StoreA', 'items': ['apple', 'banana']}, {'name': 'StoreB', 'items': ['orange']}]
    sample_list2 = [{'name': 'StoreA', 'items': ['grape', 'kiwi']}, {'name': 'StoreC', 'items': ['pear']}]
    result = merge_store_dicts(sample_list1, sample_list2)
    print(result)