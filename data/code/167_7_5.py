def initialize_store_data():
    store_data = {}
    try:
        store_data['Alice'] = 30
        if not isinstance(store_data['Alice'], int):
            raise ValueError('Age must be an integer')
        
        store_data['Bob'] = 25
        if not isinstance(store_data['Bob'], int):
            raise ValueError('Age must be an integer')

        store_data['Charlie'] = 35
        if not isinstance(store_data['Charlie'], int):
            raise ValueError('Age must be an integer')
    except ValueError as e:
        print(f'Error initializing store data: {e}')
        return None
    return store_data

if __name__ == '__main__':
    store = initialize_store_data()
    if store is not None:
        for name, age in store.items():
            print(f"Name: {name}, Age: {age}")