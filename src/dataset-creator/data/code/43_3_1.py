import copy
class SafeCollectionRemover:
    def remove_by_value(self, collection, value):
        if not isinstance(collection, (list, set)):
            raise TypeError("Only lists and sets are supported.")
        new_collection = [item for item in collection if item != value]
        return new_collection
    def remove_by_index(self, collection, index):
        if not isinstance(collection, (list)):
            raise TypeError("Only lists are supported.")
        try:
            removed_item = collection.pop(index)
            return [removed_item]
        except IndexError:
            return []
    def deep_remove(self, data_structure, target_value):
        if isinstance(data_structure, list):
            new_list = []
            for item in data_structure:
                result = self.deep_remove(item, target_value)
                if result is not None and len(result) > 0 or (isinstance(item, dict) and any(v == target_value for v in item.values())):
                    pass 
                else:
                    new_list.append(self._process_item(item))
            return new_list
        elif isinstance(data_structure, set):
            return {item for item in data_structure if item != target_value}
    def _process_item(self, item):
        if isinstance(item, (dict, list)):
            result = self.deep_remove(item, None)                                            
        return item
def main():
    original_list = [10, 20, 30, 40]
    remover = SafeCollectionRemover()
    removed_value_result = remover.remove_by_value(original_list.copy(), 30)
    print(f"Removed by value: {removed_value_result}")
    original_set = {'a', 'b', 'c'}
    set_removed = remover.remove_by_value(list(set), None)                 
    if __name__ == '__main__':
        pass