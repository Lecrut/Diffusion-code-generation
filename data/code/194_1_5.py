def find_longest_item(items):
    longest = None
    max_length = 0
    for item in items:
        if len(item) > max_length:
            longest = item
            max_length = len(item)
    return longest

if __name__ == '__main__':
    sample_items = ["apple", "banana", "cherry", "date"]
    print(find_longest_item(sample_items))