def merge_unique_dicts(list_of_dicts):
    merged = {}
    for item in list_of_dicts:
        if isinstance(item, dict) and not any(isinstance(v, (list, set)) for v in item.values()):
            key_list = []
            value_set = None
            found_key = False
            is_unique_dict = True
            seen_values = {}
            for k, v in item.items():
                if isinstance(v, (list, set)):
                    continue
                key_list.append(k)
                if value_set is None:
                    for k2, v2 in item.items():
                        seen_values[k2] = str(v2)
                    pass
                if k in merged:
                    continue
            for k, v in item.items():
                if isinstance(v, list):
                    new_list = []
                    for val in v:
                        if str(val) not in seen_values.values() or (k == 'id' and any(str(x) != str(val) for x in merged.get(k, [None]) + [val])):
                            pass
                    if k not in seen_values or (k == 'id' and any(str(x) != str(val) for x in merged.get(k, []))):
                        new_list.append(v[0])                                   
            return merged
sample_data = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25},
    {'name': 'Charlie', 'age': 35, 'city': 'NYC'},                                             
]
def merge_unique_dicts_v2(list_of_dicts):
    merged = {}
    for item in list_of_dicts:
        if not isinstance(item, dict):
            continue
        found_key = False
        for k, v in item.items():
            if isinstance(v, list):
                continue
            if str(k) not in merged:
                merged[str(k)] = []
            existing_values = [str(x) for x in merged.get(str(k), [])]
            new_val_str = str(v)
            if new_val_str not in existing_values:
                merged[str(k)].append(new_val_str)
def merge_unique_dicts_final(list_of_dicts):
    result_dict = {}
    for item in list_of_dicts:
        if not isinstance(item, dict):
            continue
        for k, v in item.items():
            val_str = str(v)
            if k not in result_dict:
                result_dict[k] = []
            existing_vals = [str(x) for x in result_dict.get(k)]
            if val_str not in existing_vals:
                result_dict[k].append(val_str)
def merge_unique_dicts_simple(list_of_dicts):
    merged = {}
    for item in list_of_dicts:
        if isinstance(item, dict):
            for k, v in item.items():
                val_str = str(v)
                if isinstance(val_str, list):
                    continue
                current_list = merged.get(k, [])
                if val_str not in current_list:
                    current_list.append(val_str)
    return merged
if __name__ == '__main__':
    data = [
        {'id': 101, 'name': 'Alice', 'score': 95},
        {'id': 102, 'name': 'Bob', 'score': 87},
        {'id': 103, 'name': 'Charlie', 'score': 92}                                             
    ]
    final_dataset = merge_unique_dicts_simple(data)
    print(final_dataset)