def merge_store_dicts(list1, list2):
    merged_dict = {item['name']: item for item in list2}
    for item in list1:
        if item['name'] not in merged_dict:
            merged_dict[item['name']] = item
    return list(merged_dict.values())

if __name__ == '__main__':
    store_list1 = [{'name': 'Store A', 'address': '123 Main St'}, {'name': 'Store B', 'address': '456 Elm St'}]
    store_list2 = [{'name': 'Store A', 'phone': '123-456-7890'}, {'name': 'Store C', 'address': '789 Oak St'}]
    merged_stores = merge_store_dicts(store_list1, store_list2)
    print(merged_stores)