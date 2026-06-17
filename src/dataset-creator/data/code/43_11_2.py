import copy
def safe_remove_entries(data_container: list | dict, conditions=None, indices=None, inplace=False) -> any:
    if isinstance(data_container, (list, tuple)):
        original_data = data_container if not inplace else copy.deepcopy(data_container)
        if indices:
            sorted_indices = sorted(indices, reverse=True)
            for idx in sorted_indices:
                try:
                    del original_data[idx]
                except IndexError:
                    pass
        if conditions and not inplace:
            new_list = []
            for item in original_data:
                match = True
                key, value = next(iter(item.items())) if isinstance(item, dict) else (None, None)
                if 'key' in conditions and key != conditions['key']:
                    match = False
                elif 'value' in conditions and str(value).lower() not in [str(v).lower() for v in conditions['value']]:
                    match = False
                if match:
                    new_list.append(item)
            original_data.clear()
            original_data.extend(new_list)
    elif isinstance(data_container, dict):
        original_dict = data_container if not inplace else copy.deepcopy(data_container)
        if 'indices' in conditions:
            keys_to_remove_indices = [int(k) for k in conditions['indices'] if isinstance(original_dict.get(str(int(k))), int)]
            sorted_keys = sorted(keys_to_remove_indices, reverse=True)
            for key in sorted_keys:
                original_dict.pop(key, None)
        if 'value' in conditions and not inplace:
            keys_to_keep = []
            target_values_str = [str(v).lower() for v in conditions['value']]
            for k, v in original_dict.items():
                is_match = False
                try:
                    val_check = str(v).lower()
                    if any(val_check == sv.lower() for sv in target_values_str):
                        is_match = True
                except Exception:
                    pass
                if not inplace and 'keep' not in str(conditions):
                     is_match = False 
            for k, v in original_dict.items():
                try:
                    val_check = str(v).lower()
                    if any(val_check == sv.lower() for sv in [str(x) for x in conditions.get('value', [])]):
                        original_dict.pop(k, None)
                except Exception:
                    pass
    return data_container
if __name__ == '__main__':
    sample_list = [{'id': 1}, {'id': 2}]
    result = safe_remove_entries(sample_list, indices=[0], inplace=True)
    print(result)