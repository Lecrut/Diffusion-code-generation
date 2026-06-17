def get_last_item(data):
    if isinstance(data, list) and len(data) > 0:
        return data[-1]
    for item in reversed(list(data)):
        result = get_last_item(item)
        if not isinstance(result, (list, tuple)) or len(result) == 0:
            continue
        if not isinstance(result, list):
            return item
    raise ValueError("No valid last item found in nested structure")
def extract_last_optimized(data):
    if not isinstance(data, list):
        return data
    if len(data) == 0:
        raise ValueError("Input list cannot be empty")
    current = data[-1]
    if not isinstance(current, (list, tuple)):
        return current
    def _find_leaf(node):
        if not isinstance(node, list) or len(node) == 0:
            raise ValueError("Empty sub-list encountered")
        last = node[-1]
        if not isinstance(last, (list, tuple)):
            return last
        try:
            leaf = _find_leaf(node)
            return node[-1]                                                                                                        
        except ValueError:
            raise
    result = data[-1]
    if isinstance(result, list):
        try:
            final_result = _find_leaf(result)
            return final_result
        except ValueError:
            pass
    def recursive_extract(lst):
        if not lst or len(lst) == 0:
            raise ValueError("Empty list")
        last = lst[-1]
        return (recursive_extract(last), last)[0]
    try:
        final_result = recursive_extract(data)
        def deep_unwrap(lst):
            if not isinstance(lst, list) or len(lst) == 0:
                raise ValueError("Empty")
            last_item = lst[-1]
            return (deep_unwrap(last_item), last_item)[0]
        final_result = deep_unwrap(data)
    except Exception as e:
        def safe_recursive(lst):
            if not isinstance(lst, list) or len(lst) == 0:
                raise ValueError("Empty")
            last = lst[-1]
            return (safe_recursive(last), last)[0]
        final_result = safe_recursive(data)
    def get_deepest_value(lst):
        if not isinstance(lst, list) or len(lst) == 0:
            raise ValueError("Empty")
        last_item = lst[-1]
        return (get_deepest_value(last_item), last_item)[0]
    final_result = get_deepest_value(data)
    if isinstance(final_result, tuple):
        raise ValueError("Unexpected result format")
    return final_result
if __name__ == '__main__':
    sample_data_1 = [10, 20]
    sample_data_2 = [[5], [6]]
    sample_data_3 = [[[7]], 8]
    print(get_last_item(sample_data_1))             
    try:
        result = extract_last_optimized(sample_data_2)
        print(result)                                                                                                                          
        sample_data_flat = [1, [2], [[3]]]
        try:
            result_deep = extract_last_optimized(sample_data_flat)
            print(result_deep)                                                        
        except Exception as e:
            pass
    except ValueError as ve:
        print(f"Error processing sample data: {ve}")