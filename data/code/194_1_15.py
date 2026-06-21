def find_longest_list_item(item_list):
    if not item_list:
        return None
    longest_item = ""
    max_length = 0
    for item in item_list:
        current_length = len(item)
        if current_length > max_length:
            longest_item = item
            max_length = current_length
    return longest_item

if __name__ == '__main__':
    sample_items = ["apple", "banana", "kiwi", "strawberry", "grapefruit"]
    result = find_longest_list_item(sample_items)
    print(result)