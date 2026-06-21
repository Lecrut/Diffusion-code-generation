def initialize_store_data():
    store_data = {}
    
    try:
        store_data['Alice'] = 30
        store_data['Bob'] = 25
        store_data['Charlie'] = 35
        
        if not isinstance(store_data, dict):
            raise TypeError("Data structure is not a dictionary")
        
        for name, age in store_data.items():
            if not isinstance(name, str) or not isinstance(age, int):
                raise ValueError(f"Invalid data: {name} - {age}")
    
    except (TypeError, ValueError) as e:
        print(e)
        return None
    
    return store_data

if __name__ == '__main__':
    store = initialize_store_data()
    if store is not None:
        print(store)