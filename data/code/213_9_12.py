def is_list(element):
    return isinstance(element, list)

def flatten_nested_list(nested_list):
    flattened = []
    for item in nested_list:
        if is_list(item):
            flattened.extend(flatten_nested_list(item))
        else:
            flattened.append(item)
    return flattened

if __name__ == '__main__':
    sample_list = [1, [2, 3], [4, [5, 6]], 7]
    print(flatten_nested_list(sample_list))