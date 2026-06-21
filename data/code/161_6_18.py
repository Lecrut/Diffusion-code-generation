from collections import namedtuple

Item = namedtuple('Item', ['name', 'quantity'])

def create_inventory(items):
    return [Item(name, quantity) for name, quantity in items]

def validate_items(items):
    if not all(isinstance(item, tuple) and len(item) == 2 for item in items):
        raise ValueError("Invalid input. Each item must be a tuple of (name, quantity).")
    if not all(isinstance(name, str) and isinstance(quantity, int) for name, quantity in items):
        raise ValueError("Invalid input. Name must be a string and quantity must be an integer.")

def main():
    sample_items = [('apple', 10), ('banana', 5), ('orange', 8)]
    try:
        validate_items(sample_items)
        inventory = create_inventory(sample_items)
        for item in inventory:
            print(f"{item.name}: {item.quantity}")
    except ValueError as e:
        print(e)

if __name__ == '__main__':
    main()