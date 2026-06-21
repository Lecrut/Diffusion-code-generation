MAX_AGE = 120

def initialize_store_data():
    store_data = {}
    try:
        add_store_data(store_data, "Alice", 30)
        add_store_data(store_data, "Bob", 25)
        add_store_data(store_data, "Charlie", 35)
    except ValueError as e:
        print(f'Error initializing store data: {e}')
    return store_data

def add_store_data(data_store, store_name, age):
    if not isinstance(store_name, str):
        raise ValueError('Name must be a string')
    if not isinstance(age, int) or age < 0 or age > MAX_AGE:
        raise ValueError(f'Age must be an integer between 0 and {MAX_AGE}')
    data_store[store_name] = age

if __name__ == '__main__':
    store_data = initialize_store_data()
    if store_data is not None:
        print(store_data)