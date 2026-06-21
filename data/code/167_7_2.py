def initialize_store_data():
    store_data = {}
    try:
        if not isinstance('Alice', str):
            raise ValueError('Name must be a string')
        if not isinstance(30, int) or 0 > 30 > 120:
            raise ValueError('Age must be an integer between 0 and 120')
        store_data['Alice'] = 30
        if not isinstance('Bob', str):
            raise ValueError('Name must be a string')
        if not isinstance(25, int) or 0 > 25 > 120:
            raise ValueError('Age must be an integer between 0 and 120')
        store_data['Bob'] = 25
    except ValueError as e:
        print(f'Error initializing store data: {e}')
    return store_data
if __name__ == '__main__':
    store_data = initialize_store_data()
    print(store_data)