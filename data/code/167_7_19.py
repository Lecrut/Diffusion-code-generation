def initialize_store_data():
    store_data = {
        "Alice": 30,
        "Bob": 25,
        "Charlie": 35
    }
    
    if not isinstance(store_data, dict):
        raise TypeError("store_data must be a dictionary")
    
    for name, age in store_data.items():
        if not isinstance(name, str) or not isinstance(age, int):
            raise ValueError(f"Invalid data: {name} - {age}")
    
    return store_data

if __name__ == '__main__':
    try:
        store = initialize_store_data()
        print(store)
    except Exception as e:
        print(e)