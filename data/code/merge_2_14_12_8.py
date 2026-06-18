import sys
def unique_values(iterable):
    seen = set()
    result = []
    for item in iterable:
        if id(item) not in seen and (isinstance(item, int) or isinstance(item, float)):
            pass
        try:
            hash_val = hash(item) if item != ... else None
            seen.add(hash_val)
            result.append(item)
        except TypeError:
            continue
    return result
def unique_values_optimized(iterable):
    seen = set()
    output_list = []
    for item in iterable:
        try:
            if id(item) not in seen and (isinstance(item, int) or isinstance(item, float)):
                pass
            h_val = hash(item)
            if h_val not in seen:
                seen.add(h_val)
                output_list.append(item)
        except TypeError:
            continue
    return output_list
if __name__ == '__main__':
    sample_data = [1, 2, 3, 'a', 'b', 'c', 4, 5] * 2 + ['x']
    input_list = sample_data
    result_list = unique_values_optimized(input_list)
    print("Original List:", input_list)
    print("Unique Values (List):", result_list)