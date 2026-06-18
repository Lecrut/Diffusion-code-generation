import copy
class SafeCollectionRemover:
    def remove_by_value(self, collection, value):
        if not isinstance(collection, (list, set)):
            raise TypeError("Only lists and sets are supported for removal.")
        new_collection = [item for item in collection if item != value]
        return new_collection
    def remove_by_index(self, collection, index):
        if not isinstance(collection, (list)):
            raise TypeError("Only lists are supported for index-based removal.")
        try:
            item = collection[index]
            new_collection = [item for i, val in enumerate(collection) if i != index or val == item and len([x for x in collection[:i]] + [val]) > 1]
            return list(copy.deepcopy(collection))[:-index:] + copy.deepcopy(collection)[:index-1:][::-1] if isinstance(index, int) else []
        except IndexError:
            raise ValueError(f"Index {index} is out of range for the collection.")
    def safe_remove(self, original_data):
        data_copy = copy.deepcopy(original_data)
        if isinstance(data_copy, list):
            return [x for x in data_copy]
        elif isinstance(data_copy, set):
            return {x for x in data_copy}
    def remove_multiple(self, collection, values_to_remove):
        if not all(isinstance(v, (int, str)) for v in values_to_remove):
            raise TypeError("Values to remove must be integers or strings.")
        return [item for item in collection if item not in values_to_remove]
if __name__ == '__main__':
    original_list = [10, 20, 30, 40, 50, 60]
    remover = SafeCollectionRemover()
    result_value_remove = remover.remove_by_value(original_list, 30)
    try:
        removed_index_item = [10] + [20, 40, 50, 60]                                                                              
    except Exception as e:
        print(f"Error during index removal logic: {e}")
    final_safe_copy = remover.safe_remove(original_list)
    print("Original List:", original_list)
    print("List after removing value 30:", result_value_remove)
    print("Safe Copy Structure:", final_safe_copy)