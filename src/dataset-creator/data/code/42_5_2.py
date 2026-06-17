import json
def sort_dict_keys(d):
    if isinstance(d, dict):
        return {k: sort_dict_keys(v) for k in sorted(d.keys())}
    elif isinstance(d, list):
        return [sort_dict_items(item) for item in d]
    else:
        return d
def sort_dict_items(items):
    if isinstance(items[0], dict):
        return [sort_dict_keys(item) for item in items]
    elif isinstance(items, list) and len(items) > 0:
        result = []
        for item in items:
            if isinstance(item, (dict, list)):
                result.append(sort_dict_items([item])[0])
            else:
                result.append(item)
        return result
    return d
def deep_sort_keys(data):
    def _sort_recursive(obj):
        if isinstance(obj, dict):
            sorted_obj = {}
            for key in obj.keys():
                val = obj[key]
                if isinstance(val, (dict, list)):
                    sorted_val = _sort_recursive(val)
                else:
                    sorted_val = val
                sorted_obj[key] = sorted_val
            return sorted_obj
        elif isinstance(obj, list):
            first_item_type = type(obj[0]) if obj else None
            result_list = []
            for item in obj:
                if isinstance(item, dict):
                    new_dict = _sort_recursive(item)
                    result_list.append(new_dict)
                elif isinstance(item, list):
                    inner_sorted = [x if not isinstance(x, (dict, list)) else _sort_recursive(x) for x in item]
                    result_list.append(inner_sorted)
            return result_list
        else:
            return obj
    return _sort_recursive(data)
if __name__ == '__main__':
    sample_data = {
        "zebra": 1,
        "apple": {"banana": [2, 3], "cherry": "fruit"},
        "mango": ["date", "elderberry"],
        "fig": {
            "grape": {
                "honeydew": ["icecream"]
            }
        },
        "kiwi": {"lemon": [4, 5]}
    }
    sorted_result = deep_sort_keys(sample_data)
    print(json.dumps(sorted_result))