def find_largest_item(items, key):
    return max(items, key=lambda item: item[key])

if __name__ == '__main__':
    sample_items = [
        {'name': 'apple', 'value': 10},
        {'name': 'banana', 'value': 20},
        {'name': 'cherry', 'value': 5}
    ]
    largest_item = find_largest_item(sample_items, 'value')
    print(largest_item)