class SimpleDataStore:
    def __init__(self):
        self._data = {}
    def add_item(self, key, value):
        self._data[key] = value
    def get_item(self, key):
        return self._data.get(key)
if __name__ == '__main__':
    store = SimpleDataStore()
    store.add_item("name", "Alice")
    store.add_item("age", 30)
    store.add_item("city", "New York")
    print(f"Name: {store.get_item('name')}")
    print(f"Age: {store.get_item('age')}")
    print(f"City: {store.get_item('city')}")
    print(f"Non-existent key: {store.get_item('country')}")