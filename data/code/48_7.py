def flatten_nested_list(nested_list):
    flat_list = []
    stack = [nested_list]
    while stack:
        current = stack.pop()
        if isinstance(current, list):
            stack.extend(reversed(current))
        else:
            flat_list.append(current)
    return flat_list

def get_largest_value(nested_list):
    if not nested_list:
        return None
    flat_list = flatten_nested_list(nested_list)
    if not flat_list:
        return None
    return max(flat_list)

if __name__ == '__main__':
    sample_data = [1, [2, 3, [4, 5]], 6, [7, [8, [9, 10]]], 11]
    result = get_largest_value(sample_data)
    print(result)