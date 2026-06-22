def min_in_nested_list(nested_list):
    flattened = [item for sublist in nested_list for item in (min_in_nested_list(sublist) if isinstance(item, list) else item)]
    return min(flattened)

if __name__ == '__main__':
    sample = [[1, 2, [3]], 4, [5, 6], 7]
    print(min_in_nested_list(sample))