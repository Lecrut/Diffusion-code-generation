items = [
    {'id': 101, 'name': 'Apple', 'quantity': 30},
    {'id': 102, 'name': 'Banana', 'quantity': 45},
    {'id': 103, 'name': 'Cherry', 'quantity': 75}
]

def print_items(item_list):
    for item in item_list:
        print(f"ID: {item['id']}, Name: {item['name']}, Quantity: {item['quantity']}")

if __name__ == '__main__':
    print("List of items:")
    print_items(items)