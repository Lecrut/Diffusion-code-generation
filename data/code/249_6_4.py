def find_largest_item_by_key(items, key):
    return max(items, key=lambda item: item[key])

if __name__ == '__main__':
    items = [
        {'name': 'apple', 'weight': 150},
        {'name': 'banana', 'weight': 80},
        {'name': 'cherry', 'weight': 20}
    ]
    largest_item = find_largest_item_by_key(items, 'weight')
    print(largest_item)