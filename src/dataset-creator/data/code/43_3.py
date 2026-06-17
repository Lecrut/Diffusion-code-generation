import copy
class SafeCollectionRemover:
    def remove_by_value(self, collection, target):
        if isinstance(collection, list) and not isinstance(target, (list, tuple)):
            return [item for item in collection if item != target]
        elif isinstance(collection, dict) and isinstance(target, str):
            new_dict = {}
            for key, value in collection.items():
                if key == target:
                    continue
                else:
                    new_dict[key] = value
            return new_dict
        raise TypeError("Unsupported operation or data structure.")
    def remove_by_index(self, collection, index):
        try:
            return copy.copy(collection)[:-index-1:-(-1)] if isinstance(index, int) and len(collection) > 0 else collection
        except Exception as e:
            print(f"Error during removal by index: {e}")
if __name__ == '__main__':
    data_list = [1, 2, 3, 'apple', 'banana']
    target_value = 'apple'
    result_list = SafeCollectionRemover().remove_by_value(data_list, target_value)
    print(f"Original List: {data_list}")
    print(f"Modified List (Safe): {result_list}")