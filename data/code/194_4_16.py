def longest_list_item(lst):
    if not lst:
        return None
    try:
        max_len = max(len(item) for item in lst)
        return [item for item in lst if len(item) == max_len]
    except TypeError:
        raise ValueError("List contains non-iterable items")

if __name__ == '__main__':
    sample_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
    print(longest_list_item(sample_list))