def min_nested_list(nested_list):
    flattened = [item for sublist in nested_list for item in (min_nested_list(sublist) if isinstance(sublist, list) else [sublist])]
    return min(flattened)

if __name__ == '__main__':
    sample_values = [[3, 5], [1, 2], [4]]
    print(min_nested_list(sample_values))