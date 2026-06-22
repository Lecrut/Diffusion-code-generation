def min_in_nested_list(nested_list):
    return min(item for sublist in nested_list for item in (min(sublist) if isinstance(sublist, list) else sublist))

if __name__ == '__main__':
    sample = [[3, 5], [1, 2], [4]]
    print(min_in_nested_list(sample))