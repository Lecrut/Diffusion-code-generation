def merge_store_dicts(list1, list2):
    dict2 = {d['name']: d for d in list2}
    result = []
    for item in list1:
        if item['name'] in dict2:
            merged_item = dict2[item['name']]
            merged_item.update(item)
            result.append(merged_item)
        else:
            result.append(item)
    return result

if __name__ == '__main__':
    store_list1 = [{'name': 'StoreA', 'address': '123 Main St'}, {'name': 'StoreB', 'address': '456 Elm St'}]
    store_list2 = [{'name': 'StoreA', 'phone': '123-456-7890'}, {'name': 'StoreC', 'address': '789 Oak St'}]
    merged_stores = merge_store_dicts(store_list1, store_list2)
    print(merged_stores)