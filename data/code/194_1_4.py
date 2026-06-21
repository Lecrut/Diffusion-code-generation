def find_longest_item(items):
    longest = None
    for item in items:
        if longest is None or len(item) > len(longest):
            longest = item
    return longest

if __name__ == '__main__':
    sample_items = ["apple", "banana", "cherry", "date"]
    print(find_longest_item(sample_items))