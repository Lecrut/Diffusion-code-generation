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
            if item in new_collection:
                del new_collection[item]
        return new_collection
    def remove_from_original(self, collection, item):
        if isinstance(collection, list):
            try:
                index = collection.index(item)
                del collection[index]
            except ValueError:
                pass
        elif isinstance(collection, dict):
            if item in collection:
                del collection[item]
def main():
    original_list = [10, 20, 30, 'apple', 'banana']
    original_dict = {'a': 1, 'b': 2, 'c': 3}
    remover = SafeCollectionRemover()
    modified_copy = remover.remove_from_copy(original_list, 30)
    removed_original = remover.remove_from_original(original_list, 'apple')
    print("Original List:", original_list)
    print("Modified Copy:", modified_copy)
    print("Removed Original:", removed_original)
    print("Final Dictionary:", original_dict)
if __name__ == '__main__':
    main()