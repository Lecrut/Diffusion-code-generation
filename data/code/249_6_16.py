def find_largest_item(items, key):
    if not items:
        return None
    largest = items[0]
    for item in items[1:]:
        if item[key] > largest[key]:
            largest = item
    return largest

if __name__ == '__main__':
    sample_items = [
        {'name': 'banana', 'calories': 95},
        {'name': 'apple', 'calories': 95},
        {'name': 'cherry', 'calories': 7}
    ]
    largest_item = find_largest_item(sample_items, 'calories')
    print(largest_item)