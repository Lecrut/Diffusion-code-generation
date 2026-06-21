def longest_item(items):
    return max(map(str, items), key=len)

if __name__ == '__main__':
    sample_items = [123, 'hello', 456789, 'world!', {'a': 1}, [1, 2, 3]]
    print(longest_item(sample_items))