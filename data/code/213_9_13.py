def flatten(nested_list):
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result
if __name__ == '__main__':
    sample = [1, [2, 3], [4, [5, 6]], 7]
    print(flatten(sample))