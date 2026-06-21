def initialize_store_data():
    store_data = {}
    try:
        if not isinstance('Alice', str) or not isinstance(30, int):
            raise ValueError('Invalid data types')
        store_data['Alice'] = 30
        if not isinstance('Bob', str) or not isinstance(25, int):
            raise ValueError('Invalid data types')
        store_data['Bob'] = 25
    except ValueError as e:
        print(f'Error: {e}')
    return store_data
if __name__ == '__main__':
    store_data = initialize_store_data()
    print(store_data)