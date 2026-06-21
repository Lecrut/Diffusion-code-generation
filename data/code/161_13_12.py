def generate_item_dicts():
    item_dict_list = [
        {'id': 1, 'name': 'Laptop', 'price': 999},
        {'id': 2, 'name': 'Mouse', 'price': 30},
        {'id': 3, 'name': 'Keyboard', 'price': 75},
        {'id': 4, 'name': 'Monitor', 'price': 150},
        {'id': 5, 'name': 'USB Cable', 'price': 25}
    ]
    return item_dict_list

if __name__ == '__main__':
    items = generate_item_dicts()
    for item in items:
        print(f"ID: {item['id']}, Name: {item['name']}, Price: ${item['price']}")