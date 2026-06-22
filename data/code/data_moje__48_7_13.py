def flatten(nested_list):
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

def get_largest_value(nested_list):
    flat_list = flatten(nested_list)
    return max(flat_list)

if __name__ == '__main__':
    sample_data = [1, [2, 3], [4, [5, [6, 7]]], 8]
    result = get_largest_value(sample_data)
    print(result)