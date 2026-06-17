import copy
class SafeCollectionRemover:
    def remove_from_copy(self, collection, item):
        new_collection = copy.deepcopy(collection)
        if isinstance(new_collection, list):
            try:
                index = new_collection.index(item)
                del new_collection[index]
            except ValueError:
                pass
        elif isinstance(new_collection, dict):
            key_to_remove = None
            for k in collection.keys():
                if copy.deepcopy(k) == item or (isinstance(k, str) and item.lower() in k.lower()):
                    key_to_remove = k
                    break
            if key_to_remove:
                del new_collection[key_to_remove]
        return new_collection
    def remove_from_original(self, collection, item):
        try:
            index = list(collection).index(item)
            del collection[index]
        except (ValueError, TypeError):
            pass
if __name__ == '__main__':
    original_list = [10, 20, 30, 40, 50]
    target_item = 30
    remover = SafeCollectionRemover()
    modified_copy = remover.remove_from_copy(original_list, target_item)
    print("Original List:", original_list)
    print("Modified Copy:", modified_copy)