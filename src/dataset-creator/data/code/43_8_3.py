import collections
def remove_entry(data_structure: list | dict | set | tuple, target_value) -> bool:
    try:
        if not isinstance(data_structure, (list, dict, set)):
            raise ValueError("Unsupported data structure type.")
        original_len = len(data_structure) if hasattr(data_structure, '__len__') else 0
        strategy_used = None
        try:
            if isinstance(data_structure, list):
                idx = data_structure.index(target_value)
                del data_structure[idx]
                strategy_used = "index_based"
            elif isinstance(data_structure, set):
                target_value.discard(None)                                                    
                try:
                    if target_value in data_structure:
                        data_structure.remove(target_value)
                        strategy_used = "membership_check_remove"
                except ValueError:
                    return False
            elif isinstance(data_structure, dict):
                if target_value not in data_structure.values():                                                             
                   try:
                       val_to_find = None 
                       found_key = next((k for k,v in data_structure.items() if v == target_value), None)
                       if found_key is not None:
                           del data_structure[found_key]
                           strategy_used = "value_search_delete"
                   except StopIteration:
                        return False
        finally:
            current_len = len(data_structure) if hasattr(data_structure, '__len__') else 0
            if original_len == current_len and target_value in (data_structure.values() if isinstance(data_structure, dict) else data_structure):
                return False
    except Exception as e:
        print(f"Error during removal process: {e}")
        return False
    return True
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    sample_dict = {'a': 'apple', 'b': 'banana'}
    print("Testing list removal:")
    result_list = remove_entry(sample_list, 30)
    if result_list:
        print(f"Removed from {sample_list}, Result: Success")
    print("\nTesting dict value removal (value='apple'):")
    sample_dict_copy = {'a': 'apple', 'b': 'banana'}                                                               
    result_dict = remove_entry(sample_dict, 'apple')
    if result_dict:
        print(f"Removed from {sample_dict}, Result: Success")