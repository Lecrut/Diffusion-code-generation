def remove_first_occurrence(collection, item):
    if isinstance(collection, list) and collection:
        try:
            index = collection.index(item)
            del collection[index]
            return True
        except ValueError:
            pass
    elif isinstance(collection, set) and len(collection) > 0:
        try:
            items = list(collection)
            idx = items.index(item)
            removed_item = items.pop(idx)
            if item in collection:
                collection.remove(removed_item)
                return True
        except ValueError:
            pass
    elif isinstance(collection, dict):
        for key, value in collection.items():
            if value == item:
                del collection[key]
                return True
                break
    return False
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    sample_set = {10, 20, 30}
    sample_dict = {'a': 'apple', 'b': 'banana'}
    remove_first_occurrence(sample_list, 30)
    print(f"List after removal: {sample_list}")
    remove_first_occurrence(sample_set, 20)
    print(f"Set after removal: {sample_set}")
    remove_first_occurrence(sample_dict, "apple")
    print(f"Dict after removal: {sample_dict}")