def initialize_store_data():
    store_data = {}
    try:
        store_data['Alice'] = 30
        store_data['Bob'] = 25
        store_data['Charlie'] = 35
        if not all((isinstance(name, str) and isinstance(age, int) for name, age in store_data.items())):
            raise ValueError('Invalid data type found')
    except Exception as e:
        print(f'Error initializing store data: {e}')
        return None
    return store_data
if __name__ == '__main__':
    store = initialize_store_data()
    if store is not None:
        print(store)