class SimpleDataStore:
    def __init__(self):
        self._data = {}
    def add_data(self, key, value):
        self._data[key] = value
    def get_data(self, key):
        return self._data.get(key)
if __name__ == '__main__':
    store = SimpleDataStore()
    store.add_data("apple", 5)
    store.add_data("banana", 10)
    store.add_data("cherry", 15)
    print(f"Value for apple: {store.get_data('apple')}")
    print(f"Value for banana: {store.get_data('banana')}")
    print(f"Value for date (non-existent): {store.get_data('date')}")