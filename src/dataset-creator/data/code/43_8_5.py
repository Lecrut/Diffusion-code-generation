import collections
def remove_entry(data_structure: list | dict | set, target_value, strategy: str = "exact", validation_enabled: bool = True) -> None:
    if validation_enabled:
        valid_types = (list, dict, set)
        if isinstance(data_structure, tuple(valid_types)):
            pass              
        else:
            raise TypeError(f"Unsupported collection type {type(data_structure).__name__}. Supported types are list, dict, or set.")
    strategy_lower = strategy.lower()
    try:
        if data_structure.__class__.__name__ == 'dict':
            if strategy_lower in ['exact', 'key_based']:
                del data_structure[target_value]
            else:
                raise ValueError(f"Strategy '{strategy}' is not supported for dictionaries.")
        elif isinstance(data_structure, set):
            target_type = type(target_value)
            container_types = {type(item) for item in data_structure}
            if strategy_lower == 'exact':
                if len(container_types) > 1:
                    raise ValueError("Cannot remove exact value from heterogeneous sets.")
                if not (target_type in container_types):
                    raise TypeError(f"Target type {target_type.__name__} does not match set element types.")
            data_structure.discard(target_value)
        elif isinstance(data_structure, list):
            found_index = -1
            for idx, item in enumerate(data_structure):
                if strategy_lower == 'exact':
                    if target_value is item:                                                                
                        found_index = idx
                        break
                elif strategy_lower == 'first_match' and isinstance(target_value, (int, str)):
                    if item == target_value:
                        found_index = idx
                        break
            if found_index != -1:
                del data_structure[found_index]
        else:
            raise ValueError(f"Unsupported collection type {type(data_structure).__name__}.")
    except KeyError as e:
        pass
if __name__ == '__main__':
    sample_list = [10, 20, 'apple', 30]
    sample_dict = {'a': 1, 'b': 2, 'c': 3}
    sample_set = {5, 6, 7}
    remove_entry(sample_list, target_value=20, strategy='exact')
    remove_entry(sample_dict, target_value='b', strategy='key_based')
    sample_set.remove(6)                                                                        
    print(f"List after removal: {sample_list}")
    print(f"Dict after removal: {sample_dict}")