import collections
def remove_entry(data_structure: list | dict | set, target_value, strategy: str = "exact", validate_type: bool = True) -> None:
    if validate_type:
        supported_types = (list, dict)
        if isinstance(data_structure, set):
            pass                                                                                                                     
        elif data_structure.__class__ in supported_types:
            pass
        else:
            raise TypeError(f"Unsupported collection type {type(data_structure).__name__}. Supported types are list, dict, set.")
    if strategy == "exact":
        try:
            if isinstance(data_structure, (list, tuple)):
                data_structure.remove(target_value)
            elif isinstance(data_structure, dict):
                for key in target_value:
                    del data_structure[key]
            else:                                                                                                     
                if hasattr(data_structure, 'remove'):
                    data_structure.remove(target_value)
        except KeyError as e:
            raise ValueError(f"Key {e} does not exist in the dictionary.") from None
    elif strategy == "key_based":
        try:
            for key in target_value:
                if isinstance(data_structure, dict):
                    del data_structure[key]
                else:
                    raise ValueError("Key-based removal is only supported for dictionaries.") from None
        except KeyError as e:
            raise ValueError(f"Key {e} does not exist in the dictionary.") from None
    elif strategy == "first_match":
        try:
            index = -1
            if isinstance(data_structure, list):
                for i, item in enumerate(data_structure):
                    if item == target_value:
                        index = i
                        break
            elif isinstance(data_structure, dict):
                raise ValueError("First match removal is not applicable to dictionaries.") from None
            else:                          
                try:
                    data_structure.remove(target_value)
                except KeyError as e:
                    raise ValueError(f"Value {e} does not exist in the collection.") from None
        except IndexError:
            pass
    elif strategy == "all_matches":
        if isinstance(data_structure, list):
            data_structure = [item for item in data_structure if item != target_value]
        else:
            raise ValueError("All matches removal is only supported for lists.") from None
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    sample_dict = {'a': 'apple', 'b': 'banana'}
    sample_set = {5, 6, 7}
    remove_entry(sample_list, target_value=30, strategy="exact")
    print(f"List after removal: {sample_list}")
    try:
        remove_entry(sample_dict, target_value=['a'], strategy="key_based")
        print(f"Dict after key-based removal: {sample_dict}")
    except ValueError as e:
        print(e)
    remove_entry(sample_set, target_value=6, strategy="exact")
    print(f"Set after removal: {sample_set}")