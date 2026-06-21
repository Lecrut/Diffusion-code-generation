class StoreMerger:

    @staticmethod
    def merge_stores(list1, list2):
        merged_dict = {}
        for store in list1:
            merged_dict[store['name']] = store
        for store in list2:
            if store['name'] in merged_dict:
                merged_dict[store['name']].update(store)
            else:
                merged_dict[store['name']] = store
        return list(merged_dict.values())
if __name__ == '__main__':
    sample_list1 = [{'name': 'StoreA', 'data': 'DataA'}, {'name': 'StoreB', 'data': 'DataB'}]
    sample_list2 = [{'name': 'StoreA', 'data': 'UpdatedDataA'}, {'name': 'StoreC', 'data': 'DataC'}]
    merged_result = StoreMerger.merge_stores(sample_list1, sample_list2)
    print(merged_result)