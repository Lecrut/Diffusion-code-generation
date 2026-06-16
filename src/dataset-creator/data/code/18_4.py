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
                    for sub_item in reversed_data:
                        if isinstance(sub_item, dict):
                            temp_new_dict = {}
                            for k, v in sorted(item.items()):
                                temp_new_dict[k] = reverse_sequence(v)
                            return new_dict
                        elif isinstance(sub_item, (list, tuple)):
                            result_list.append(reverse_sequence(list(sub_item)))
                    if not any(isinstance(x, dict) or isinstance(x, list) for x in reversed_data):
                        return [reverse_sequence(item) for item in data]
                else:
                    return reverse_sequence(data)
            return []
        elif isinstance(data, (int, float)):
            return int(reversed(str(int(float(data))))) if not isinstance(data, str) else list(reversed(list(data)))
    except Exception as e:
        print(f"Error processing data: {e}")
    return None
if __name__ == '__main__':
    sample_data = [1, 2, {'a': 'b', 'c': ['d', 'e']}, (3, 4), [], "string"]
    result = reverse_sequence(sample_data)
    print(result)