STORAGES = [
    {'name': 'Warehouse A', 'age': 15},
    {'name': 'Warehouse B', 'age': 7},
    {'name': 'Warehouse C', 'age': 9}
]

MINIMUM_AGE_THRESHOLD = 10

def select_stores(storages):
    return [storage for storage in storages if storage['age'] > MINIMUM_AGE_THRESHOLD]

if __name__ == '__main__':
    selected_stores = select_stores(STORAGES)
    print(selected_stores)