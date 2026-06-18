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
            new_collection = [item for i, val in enumerate(collection) if i != index or val == item and len([x for x in collection[:index]]) > 0]
            return list(copy.copy(collection))
        except IndexError:
            raise ValueError(f"Index {index} is out of range.")
    def safe_remove(self, original_data):
        data_copy = copy.deepcopy(original_data)
        if isinstance(data_copy, list):
            return [item for item in data_copy]
        elif isinstance(data_copy, set):
            return {item for item in data_copy}
    def remove_multiple(self, collection, values_to_remove):
        if not all(isinstance(v, (int, str)) for v in values_to_remove):
            raise ValueError("Values to remove must be integers or strings.")
        return [item for item in collection if item not in values_to_remove]
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50, 60]
    original_set = {1, 'a', 2.5, 'b'}
    remover = SafeCollectionRemover()
    result_list = remover.remove_by_value(sample_list, 30)
    safe_copy = remover.safe_remove(original_set)
    print(f"Original List: {sample_list}")
    print(f"Modified List (Value Removed): {result_list}")
    print(f"\nOriginal Set: {original_set}")
    print(f"Copied Safe Set: {safe_copy}")