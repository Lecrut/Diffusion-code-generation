def flatten_list(nested_list):
    flattened = []
    for item in nested_list:
        if isinstance(item, list):
            flattened.extend(flatten_list(item))
        else:
            flattened.append(item)
    return flattened

if __name__ == '__main__':
    sample_list = [1, [2, 3], [4, [5, 6]], 7]
    result = flatten_list(sample_list)
    print(result)