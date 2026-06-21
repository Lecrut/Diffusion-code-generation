def find_longest_item(items):
    return max(map(str, items), key=len)

if __name__ == '__main__':
    sample_items = [42, "hello", 3.14, "world!", {"key": "value"}]
    print(find_longest_item(sample_items))