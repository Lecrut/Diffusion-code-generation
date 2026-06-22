MAX_KEY = 'max_key'

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
        {'name': 'apple', 'price': 1.2},
        {'name': 'banana', 'price': 0.8},
        {'name': 'cherry', 'price': 3.5}
    ]
    largest_item = find_largest_item(sample_items, MAX_KEY)
    print(largest_item)