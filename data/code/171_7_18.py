def merge_store_dicts(list1, list2):
    dict2 = {store['name']: store for store in list2}
    merged_dict = {}
    for store in list1:
        if store['name'] in dict2:
            merged_dict[store['name']] = {**dict2[store['name']], **store}
        else:
            merged_dict[store['name']] = store
    return [merged_dict[name] for name in sorted(merged_dict)]

if __name__ == '__main__':
    list1 = [{'name': 'StoreA', 'address': '123 Main St'}, {'name': 'StoreB', 'address': '456 Elm St'}]
    list2 = [{'name': 'StoreA', 'phone': '555-1234'}, {'name': 'StoreC', 'address': '789 Oak St'}]
    print(merge_store_dicts(list1, list2))