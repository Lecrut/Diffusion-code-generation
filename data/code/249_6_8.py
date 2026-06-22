def find_largest_item(items, key):
    return max(items, key=lambda item: item[key])

if __name__ == '__main__':
    sample_items = [
        {'name': 'apple', 'weight': 150},
        {'name': 'banana', 'weight': 80},
        {'name': 'cherry', 'weight': 20}
    ]
    largest_item = find_largest_item(sample_items, 'weight')
    print(largest_item)