def initialize_store_data():
    store_data = []
    try:
        if isinstance('Alice', str) and isinstance(30, int):
            store_data.append({'name': 'Alice', 'age': 30})
        if isinstance('Bob', str) and isinstance(25, int):
            store_data.append({'name': 'Bob', 'age': 25})
    except Exception as e:
        print(f'Error initializing store data: {e}')
    return store_data
if __name__ == '__main__':
    store = initialize_store_data()
    print(store)