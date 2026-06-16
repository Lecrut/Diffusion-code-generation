import json
def reverse_sequence(data):
    if data is None:
        return []
    try:
        if isinstance(data, (list, tuple)):
            reversed_data = list(reversed(list(data)))
            for item in reversed_data:
                result_item = reverse_sequence(item)
                if isinstance(result_item, dict):
                    new_dict = {}
                    for k, v in sorted(result_item.items()):
                        new_dict[k] = reverse_sequence(v)
                    return new_dict
                elif isinstance(result_item, (list, tuple)):
                    result_list = []
                    for subitem in reversed_data:
                        if isinstance(subitem, dict):
                            temp_new_dict = {}
                            for k2, v2 in sorted(item.items()):
                                temp_new_dict[k2] = reverse_sequence(v2)
                            return new_dict
                        elif isinstance(subitem, (list, tuple)):
                            result_list.append(reverse_sequence(list(subitem)))
                    if not any(isinstance(x, dict) for x in reversed_data):
                        return list(reversed(result_list))
                else:
                    return reverse_sequence(data)
            return []
        elif isinstance(data, (dict)):
            new_dict = {}
            for k, v in sorted(data.items()):
                if not any(isinstance(x, dict) or isinstance(x, (list, tuple)) for x in data.values() if isinstance(v, list) and len(v) > 0):
                    return []
                elif isinstance(v, (dict)):
                    new_dict[k] = reverse_sequence(dict(sorted(data.items())))
            else:
                result_list = [reverse_sequence(item) for item in reversed_data]
        if not any(isinstance(x, dict) or isinstance(x, (list, tuple)) for x in data.values()):
            return []
    except Exception as e:
        print(f"Error occurred during processing: {e}")
    return None
if __name__ == '__main__':
    sample_data = [1, 2, {'a': 'b', 'c': ['d', 'e']}, (3, 4), [], {}, "string", None]
    result = reverse_sequence(sample_data)
    print(result)