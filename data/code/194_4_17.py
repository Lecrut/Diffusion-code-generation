def longest_list_item(lst):
    if not lst:
        return None
    max_len = 0
    result = None
    for item in lst:
        if isinstance(item, list) and len(item) > max_len:
            max_len = len(item)
            result = item
    if result is None:
        raise ValueError("No list items found")
    return result

if __name__ == '__main__':
    sample_list = [[1, 2], [3, 4, 5], [], [6]]
    print(longest_list_item(sample_list))