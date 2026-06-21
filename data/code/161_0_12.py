items = [
    {'id': 101, 'name': 'Grape', 'price': 3.49},
    {'id': 102, 'name': 'Orange', 'price': 1.25},
    {'id': 103, 'name': 'Lemon', 'price': 0.79},
    {'id': 104, 'name': 'Mango', 'price': 4.99},
    {'id': 105, 'name': 'Peach', 'price': 2.39}
]

if __name__ == '__main__':
    print("List of items:")
    for item in items:
        print(f"ID: {item['id']}, Name: {item['name']}, Price: ${item['price']:.2f}")