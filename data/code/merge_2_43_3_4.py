import copy
class SafeCollectionRemover:
    def remove_from_copy(self, collection, item):
        try:
            new_collection = copy.deepcopy(collection)
            if isinstance(new_collection, list):
                return [x for x in new_collection if x != item]
            elif isinstance(new_collection, dict):
                return {k: v for k, v in new_collection.items() if v != item}
        except Exception as e:
            raise RuntimeError(f"Failed to create deep copy or remove item: {e}")
    def modify_in_place(self, collection, index=None, value=None):
        try:
            if isinstance(collection, list) and index is not None:
                return [collection[i] for i in range(len(collection)) if i != index or (value is not None and collection[index] == value)]
            elif isinstance(collection, dict):
                new_dict = {}
                for k, v in collection.items():
                    if value is None or v != value:
                        new_dict[k] = v
                return new_dict
        except Exception as e:
            raise RuntimeError(f"Failed to modify original collection: {e}")
if __name__ == '__main__':
    data_list = [1, 2, 3, 'apple', 'banana']
    target_item = 'apple'
    remover = SafeCollectionRemover()
    modified_copy = remover.remove_from_copy(data_list, target_item)
    print("Original list:", data_list)
    print("Modified copy:", modified_copy)