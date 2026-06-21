def initialize_store_data():
    try:
        store_data = {
            'Alice': 30,
            'Bob': 25,
            'Charlie': 35
        }
        for name, age in store_data.items():
            if not isinstance(name, str) or not isinstance(age, int):
                raise ValueError("Invalid data type")
        return store_data
    except Exception as e:
        print(f"Error initializing store data: {e}")
        return None

if __name__ == '__main__':
    store = initialize_store_data()
    if store:
        print(store)