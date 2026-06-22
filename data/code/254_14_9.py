def flatten_list(nested_list):
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result

def find_minimum(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    flattened_data = flatten_list(data)
    return min(flattened_data)

if __name__ == '__main__':
    list1 = [5, 2, [8, 1]]
    list2 = []
    try:
        result1 = find_minimum(list1)
        print(f"Minimum of {list1}: {result1}")
        find_minimum(list2)
    except ValueError as e:
        print(f"Caught expected error for empty list: {e}")