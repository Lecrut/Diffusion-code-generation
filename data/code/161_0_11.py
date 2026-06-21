ITEMS = [
    {'id': 1, 'name': 'Apple', 'price': 0.99},
    {'id': 2, 'name': 'Banana', 'price': 0.59},
    {'id': 3, 'name': 'Cherry', 'price': 2.49}
]

def print_items():
    for item in ITEMS:
        print(f"ID: {item['id']}, Name: {item['name']}, Price: ${item['price']}")

if __name__ == '__main__':
    print_items()