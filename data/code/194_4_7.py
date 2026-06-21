def longest_list_item(lst):
    if not lst:
        return None
    max_length = 0
    longest_item = None
    for item in lst:
        if isinstance(item, list) and len(item) > max_length:
            max_length = len(item)
            longest_item = item
    if longest_item is None:
        raise ValueError("No list items found")
    return longest_item

if __name__ == '__main__':
    sample_list = [[1, 2], [3, 4, 5], [], [6]]
    print(longest_list_item(sample_list))