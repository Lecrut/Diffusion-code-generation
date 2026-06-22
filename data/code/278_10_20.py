def print_items(items):
    for item in items:
        print(item)

if __name__ == '__main__':
    sample_items = {
        'fruits': ['Apple', 'Banana'],
        'numbers': [1, 2],
        'empty': []
    }
    for category, items in sample_items.items():
        print(f"Category: {category}")
        print_items(items)