def merge_store_lists(list1, list2):
    merged_dict = {store['name']: store for store in list2}
    
    for store in list1:
        if store['name'] in merged_dict:
            merged_dict[store['name']].update(store)
        else:
            merged_dict[store['name']] = store
    
    return list(merged_dict.values())

if __name__ == '__main__':
    sample_list1 = [
        {'name': 'StoreA', 'address': 'Address 1'},
        {'name': 'StoreB', 'phone': 'Phone 1'}
    ]
    
    sample_list2 = [
        {'name': 'StoreA', 'email': 'Email 1'},
        {'name': 'StoreC', 'website': 'Website 1'}
    ]
    
    result = merge_store_lists(sample_list1, sample_list2)
    print(result)