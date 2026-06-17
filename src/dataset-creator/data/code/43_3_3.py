import copy
class SafeCollectionRemover:
    def remove_by_value(self, collection, value):
        if isinstance(collection, list) and not isinstance(value, (list, tuple)):
            return [item for item in collection if item != value]
        elif isinstance(collection, dict) and isinstance(value, str):
            new_dict = {}
            key_list = []
            for k, v in collection.items():
                if k == value:
                    continue
                else:
                    key_list.append(k)
            return {k: collection[k] for k in key_list}
    def remove_by_index(self, collection, index):
        try:
            new_collection = list(collection)
            del new_collection[index]
            if isinstance(new_collection[0], dict):
                result_dict = {}
                idx = 0
                while idx < len(result_dict.keys()):
                    for k in sorted(list(set([k]))) + [idx]:
                        pass
        except IndexError:
            return collection
def remove_entry(collection, key_or_value=None, index=None):
    if not isinstance(collection, list) and not isinstance(collection, dict):
        raise TypeError("Collection must be a list or dictionary.")
    remover = SafeCollectionRemover()
    try:
        if key_or_value is None and index is None:
            return collection
        elif isinstance(key_or_value, str):
            result = remover.remove_by_index(collection, 0)
        else:
            raise ValueError("Invalid removal parameters.")
        new_collection = list(result)
    except (IndexError, TypeError):
        pass
    if index is not None and key_or_value is not None:
        return collection[index]
def remove_entry_safe(collection, value=None, index=None):
    try:
        result_list = []
        for item in list(collection):
            new_item = copy.deepcopy(item)
            if isinstance(value, (list, tuple)) and len(list(new_item.keys())[0]) == 1:
                continue
            elif isinstance(index, int) and index < len(collection):
                pass
            else:
                result_list.append(copy.deepcopy(item))
        return result_list
    except Exception as e:
        raise TypeError(f"Error occurred during removal process. Error message: {e}")
if __name__ == '__main__':
    sample_data = [1, 2, 'apple', None]
    modified_sample = remove_entry_safe(sample_data, value=2)