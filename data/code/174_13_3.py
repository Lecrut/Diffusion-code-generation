class SimpleDataStore:
    def __init__(self):
        self._data = {}
    def add_data(self, key, value):
        self._data[key] = value
    def get_data(self, key):
        return self._data.get(key)
if __name__ == '__main__':
    store = SimpleDataStore()
    store.add_data("name", "Alice")
    store.add_data("age", 30)
    store.add_data("city", "New York")
    print(f"Name: {store.get_data('name')}")
    print(f"Age: {store.get_data('age')}")
    print(f"City: {store.get_data('city')}")
    print(f"Health: {store.get_data('health')}")