def create_item_list():
    items = [
        {'id': 1, 'name': 'Laptop', 'price': 999.99},
        {'id': 2, 'name': 'Mouse', 'price': 29.99},
        {'id': 3, 'name': 'Keyboard', 'price': 49.99}
    ]
    return items

def main():
    item_list = create_item_list()
    print("List of items:")
    for item in item_list:
        print(f"ID: {item['id']}, Name: {item['name']}, Price: ${item['price']}")

if __name__ == '__main__':
    main()