def print_items(item_list):
    for item in item_list:
        print(item)

if __name__ == '__main__':
    sample_items = {'fruit': ['apple', 'banana', 'cherry'], 'vegetable': ['carrot', 'lettuce']}
    for category, items in sample_items.items():
        print(category.upper())
        print_items(items)