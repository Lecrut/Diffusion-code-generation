def create_item_dict(id, name, price):
    if not isinstance(id, int) or id <= 0:
        raise ValueError("ID must be a positive integer")
    if not isinstance(name, str) or not name.strip():
        raise ValueError("Name must be a non-empty string")
    if not isinstance(price, (int, float)) or price < 0:
        raise ValueError("Price must be a non-negative number")
    
    return {
        'id': id,
        'name': name,
        'price': price
    }

def populate_item_list():
    items = [
        create_item_dict(1, "Apple", 0.99),
        create_item_dict(2, "Banana", 0.59),
        create_item_dict(3, "Cherry", 2.49)
    ]
    return items

if __name__ == '__main__':
    item_list = populate_item_list()
    for item in item_list:
        print(item)