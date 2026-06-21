def initialize_store_data():
    store = {}
    try:
        store['Alice'] = 30
        store['Bob'] = 25
        store['Charlie'] = 35
        if not all(isinstance(age, int) for age in store.values()):
            raise ValueError("All ages must be integers")
        return store
    except Exception as e:
        print(f"Error initializing store data: {e}")
        return None

if __name__ == '__main__':
    store_data = initialize_store_data()
    if store_data is not None:
        print(store_data)