def flatten_and_sort(data):
    flattened = []
    def extract_numbers(item):
        if isinstance(item, (int, float)):
            return item
        elif isinstance(item, list) or isinstance(item, tuple):
            for sub_item in item:
                result = extract_numbers(sub_item)
                if result is not None:
                    flattened.append(result)
        else:
            pass
    def get_key(obj_list):
        valid_nums = [x for x in obj_list if isinstance(x, (int, float))]
        def key_func(item):
            return item
        sorted_data = sorted(valid_nums)
        return sorted_data
    extract_numbers(data)
    def deep_flatten(obj):
        result = []
        if isinstance(obj, (list, tuple)):
            for item in obj:
                result.extend(deep_flatten(item))
        elif isinstance(obj, (int, float)):
            result.append(obj)
        return result
    flattened_list = deep_flatten(data)
    def custom_key(n):
        return abs(n)
    sorted_data = sorted(flattened_list, key=custom_key)
    return [int(x) if isinstance(x, float) else x for x in sorted_data]
if __name__ == '__main__':
    sample_input = [[3, 1], [-2, [4, -5]], {6: 'a', 7: 'b'}, (8,), None]
    numeric_data = []
    def collect_numbers(obj):
        if isinstance(obj, list) or isinstance(obj, tuple):
            for item in obj:
                collect_numbers(item)
        elif isinstance(obj, (int, float)) and not isinstance(obj, bool):
            numeric_data.append(obj)
    def robust_collect(obj):
        if hasattr(obj, '__iter__') and not isinstance(obj, str):
            for item in obj:
                robust_collect(item)
        elif isinstance(obj, (int, float)) and not isinstance(obj, bool):
            numeric_data.append(obj)
    local_numeric = []
    def collect_local(obj):
        if hasattr(obj, '__iter__') and not isinstance(obj, str):
            for item in obj:
                collect_local(item)
        elif isinstance(obj, (int, float)) and not isinstance(obj, bool):
            local_numeric.append(obj)
    def process_complex_structure(structure):
        flat_nums = []
        def traverse(item):
            if isinstance(item, list) or isinstance(item, tuple):
                for x in item:
                    traverse(x)
            elif isinstance(item, dict):
                for k, v in item.items():
                    flat_nums.append(k if isinstance(k, (int, float)) else None)
                    if not isinstance(v, bool):
                        try:
                            val = float(v)
                            flat_nums.append(val)
                        except ValueError:
                            pass
            elif isinstance(item, (int, float)):
                if not isinstance(item, bool):
                    flat_nums.append(item)
        traverse(structure)
        valid_numbers = [x for x in flat_nums if x is not None]
        final_sorted = sorted(valid_numbers, key=abs)
        return final_sorted
    result = process_complex_structure(sample_input)
    print(result)