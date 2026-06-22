def find_largest_item(items, key):
    if not items:
        return None
    return max(items, key=lambda item: item[key])

if __name__ == '__main__':
    sample_items = [
        {'name': 'apple', 'price': 1.2},
        {'name': 'banana', 'price': 0.8},
        {'name': 'cherry', 'price': 2.5}
    ]
    largest_item = find_largest_item(sample_items, 'price')
    print(largest_item)