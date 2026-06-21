def is_list(item):
    return isinstance(item, list)

def flatten_nested_list(nested_list):
    result = []
    for item in nested_list:
        if is_list(item):
            result.extend(flatten_nested_list(item))
        else:
            result.append(item)
    return result

if __name__ == '__main__':
    sample_list = [1, [2, 3], [4, [5, 6]], 7]
    print(flatten_nested_list(sample_list))