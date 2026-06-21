def longest_item(items):
    return max(items, key=len)

if __name__ == '__main__':
    sample_items = ["apple", "banana", "cherry", "date"]
    print(longest_item(sample_items))