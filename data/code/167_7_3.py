def initialize_store_data():
    store_data = []
    try:
        store_data.append({"name": "Alice", "age": 30})
        store_data.append({"name": "Bob", "age": 25})
        store_data.append({"name": "Charlie", "age": 35})
    except TypeError as e:
        print(f"Type error occurred: {e}")
    return store_data

if __name__ == '__main__':
    store = initialize_store_data()
    for person in store:
        print(person)