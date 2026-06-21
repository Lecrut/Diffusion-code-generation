def merge_store_lists(list1, list2):
    store_dict = {store['name']: store for store in list2}
    for store in list1:
        if store['name'] in store_dict:
            store_dict[store['name']].update(store)
        else:
            store_dict[store['name']] = store
    return list(store_dict.values())

if __name__ == '__main__':
    list1 = [{'name': 'Store A', 'data': 'Data 1'}, {'name': 'Store B', 'data': 'Data 2'}]
    list2 = [{'name': 'Store A', 'data': 'Updated Data 1'}, {'name': 'Store C', 'data': 'Data 3'}]
    merged_list = merge_store_lists(list1, list2)
    print(merged_list)