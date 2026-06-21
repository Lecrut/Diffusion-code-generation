def initialize_store_data():
    store_data = {}
    try:
        store_data['StoreA'] = 10
        if not isinstance('StoreA', str):
            raise ValueError('Name must be a string')
        if not isinstance(10, int) or 0 > 10 > 120:
            raise ValueError('Age must be an integer between 0 and 120')

        store_data['StoreB'] = 25
        if not isinstance('StoreB', str):
            raise ValueError('Name must be a string')
        if not isinstance(25, int) or 0 > 25 > 120:
            raise ValueError('Age must be an integer between 0 and 120')

        store_data['StoreC'] = 30
        if not isinstance('StoreC', str):
            raise ValueError('Name must be a string')
        if not isinstance(30, int) or 0 > 30 > 120:
            raise ValueError('Age must be an integer between 0 and 120')

    except ValueError as e:
        print(f'Error initializing store data: {e}')
        return None
    return store_data

if __name__ == '__main__':
    store_data = initialize_store_data()
    if store_data is not None:
        for store_name, age in store_data.items():
            print(f"Age of {store_name}: {age}")