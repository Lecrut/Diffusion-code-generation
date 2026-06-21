def find_longest_list_item(items):
    if not items:
        return ""
    longest = items[0]
    for item in items:
        if len(item) > len(longest):
            longest = item
    return longest

if __name__ == '__main__':
    sample_items = ["pineapple", "mango", "kiwi", "strawberry", "grapefruit"]
    result = find_longest_list_item(sample_items)
    print(result)