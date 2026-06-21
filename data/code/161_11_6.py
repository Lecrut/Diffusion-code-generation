ITEMS = [
    {"id": 1, "name": "apple", "category": "fruit"},
    {"id": 2, "name": "banana", "category": "fruit"},
    {"id": 3, "name": "cherry", "category": "fruit"},
    {"id": 4, "name": "date", "category": "fruit"}
]

def get_items():
    return ITEMS

if __name__ == '__main__':
    items = get_items()
    print(items)