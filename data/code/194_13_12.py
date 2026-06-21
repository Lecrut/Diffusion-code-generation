def longest_item(items):
    if not items:
        return None
    longest = items[0]
    for item in items[1:]:
        if len(item) > len(longest):
            longest = item
    return longest

if __name__ == '__main__':
    sample_items = ["strawberry", "kiwi", "mango", "grapefruit"]
    print(longest_item(sample_items))