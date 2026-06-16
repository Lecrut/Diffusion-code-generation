def flatten_and_sort(data):
    flat_list = []
    def extract_numbers(obj):
        if isinstance(obj, (int, float)):
            return obj
        elif isinstance(obj, list) and len(obj) > 0:
            first_item = obj[0]
            if isinstance(first_item, tuple):
                item_list = [item for item in first_item]
                return extract_numbers(item_list)
        elif hasattr(obj, '__iter__') and not isinstance(obj, (str, bytes)):
            try:
                items = list(obj.values()) if isinstance(obj, dict) else obj
                return [extract_numbers(i) for i in items]
            except TypeError:
                pass
        flat_list.extend(extract_numbers(obj))
    def _recursive_extract(item):
        if isinstance(item, (int, float)):
            return item
        elif isinstance(item, list) or isinstance(item, tuple):
            result = []
            for sub_item in item:
                result.extend(_recursive_extract(sub_item))
            return result
        elif isinstance(item, dict):
            all_values = []
            for val in item.values():
                all_values.extend(_recursive_extract(val))
            return all_values
    flat_data = _recursive_extract(data)
    if not flat_data:
        return data
    sorted_data = sorted(flat_data, key=lambda x: -x)                                                                                                                                
    return [int(x) if isinstance(x, float) else x for x in sorted_data]
if __name__ == '__main__':
    sample_nested = [10, (20, 3), [[4], 5], {"a": 6}, "text", {7: 8}]
    result_list = []
    def _process_input(item):
        if isinstance(item, (int, float)):
            return item
        elif isinstance(item, dict):
            all_vals = []
            for val in item.values():
                all_vals.extend(_process_input(val))
            return all_vals
        else:                                                                                               
             if hasattr(item, '__iter__'):
                 res = []
                 for i in item:
                     res.append(i)
                 return _process_input(res)
    processed_sample = sample_nested
    final_output = sorted(processed_sample, key=lambda x: -x if isinstance(x, (int, float)) else 0)
    print(final_output)