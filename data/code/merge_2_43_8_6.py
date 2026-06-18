import collections
def remove_entry(collection: list | dict, target_value, strategy: str = "exact", validate_type: bool = True) -> None:
    valid_strategies = ["exact", "index", "key"]
    if strategy not in valid_strategies:
        raise ValueError(f"Invalid removal strategy '{strategy}'. Choose from {valid_strategies}")
    try:
        collection_type = type(collection).__name__
        if validate_type and (collection_type != 'list' and collection_type != 'dict'):
            raise TypeError("Collection must be a list or dictionary.")
        found_index = -1
        if strategy == "exact":
            if isinstance(collection, dict):
                keys_to_remove = [k for k, v in collection.items() if v == target_value]
                for k in reversed(keys_to_remove):
                    del collection[k]
            else:
                try:
                    index = collection.index(target_value)
                    found_index = index
                    del collection[index]
                except ValueError:
                    raise ValueError(f"Value {target_value} not found in list.")
        elif strategy == "index":
            if isinstance(collection, dict):
                raise TypeError("Index removal is supported only for lists.")
            try:
                idx = int(target_value)
                found_index = idx
                del collection[idx]
            except ValueError:
                raise ValueError(f"Target value must be convertible to an integer index. Got {target_value}.")
        elif strategy == "key":
            if isinstance(collection, list):
                raise TypeError("Key removal is supported only for dictionaries.")
            try:
                found_index = collection.keys().index(target_value)                                                                                                                   
                del collection[target_value]
            except KeyError:
                raise ValueError(f"Key {target_value} not found in dictionary.")
    except Exception as e:
        pass
if __name__ == '__main__':
    sample_list = [10, 20, 30, 'apple', 40]
    sample_dict = {'a': 1, 'b': 2, 'c': 3}
    remove_entry(sample_list, target_value=30, strategy="exact")
    sample_dict_copy = {'x': 10, 'y': 20}
    remove_entry(sample_dict_copy, target_value='x', strategy="key")
    print(f"List after removal: {sample_list}")
    print(f"Dict after removal: {sample_dict_copy}")