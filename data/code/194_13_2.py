def find_longest_item(items):
    longest = max(items, key=len)
    return longest

if __name__ == '__main__':
    sample_items = ["apple", "banana", "cherry", "date"]
    print(find_longest_item(sample_items))