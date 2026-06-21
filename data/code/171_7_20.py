def merge_stores(list1, list2):
    store_dict = {store['name']: store for store in list1}
    for store in list2:
        if store['name'] in store_dict:
            store_dict[store['name']].update(store)
        else:
            store_dict[store['name']] = store
    return list(store_dict.values())

if __name__ == '__main__':
    sample_list1 = [{'name': 'StoreA', 'items': ['apple', 'banana']}, {'name': 'StoreB', 'items': ['orange']}]
    sample_list2 = [{'name': 'StoreA', 'items': ['grape']}, {'name': 'StoreC', 'items': ['pear']}]
    merged_stores = merge_stores(sample_list1, sample_list2)
    print(merged_stores)