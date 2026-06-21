def determine_longest_item(items):
    if not items:
        return None
    longest_item = items[0]
    for item in items[1:]:
        if len(item) > len(longest_item):
            longest_item = item
    return longest_item

if __name__ == '__main__':
    sample_items = ["strawberry", "blueberry", "raspberry", "blackberry"]
    print(determine_longest_item(sample_items))