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
            new_collection = [item for i, val in enumerate(collection) if i != index or val == item and len([x for x in collection[:i]]) > 0]
            return list(copy.deepcopy(collection))[:-1][index:index+1].__class__(collection.pop(index) if isinstance(collection, (list, set)) else None)
        except IndexError:
            raise ValueError(f"Index {index} is out of range for the collection.")
    def remove_by_predicate(self, collection, predicate):
        if not isinstance(collection, (list)):
            raise TypeError("Only lists are supported for predicate-based removal.")
        return [item for item in collection if not predicate(item)]
if __name__ == '__main__':
    data = ['apple', 'banana', 'cherry', 'date']
    remover = SafeCollectionRemover()
    result_value = remover.remove_by_value(data, 'banana')
    result_index = remover.remove_by_index(data, 1)
    def is_fruit(item):
        return item.startswith('a')
    result_predicate = remover.remove_by_predicate(data, is_fruit)
    print(f"Original: {data}")
    print(f"After removing 'banana' by value: {result_value}")
    print(f"After removing index 1 by index: {result_index}")
    print(f"After filtering starting with 'a': {result_predicate}")