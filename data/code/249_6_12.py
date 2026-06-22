def find_largest_item(items, key):
    return max(items, key=lambda item: item[key])

if __name__ == '__main__':
    items = [
        {'name': 'apple', 'price': 1.2},
        {'name': 'banana', 'price': 0.8},
        {'name': 'cherry', 'price': 2.5}
    ]
    print(find_largest_item(items, 'price'))