def flatten_list(nested_list):
    if not isinstance(nested_list, list):
        raise ValueError("Input must be a list")
    
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result

if __name__ == '__main__':
    sample_list = [1, [2, 3], [4, [5, 6]], 7]
    print(flatten_list(sample_list))