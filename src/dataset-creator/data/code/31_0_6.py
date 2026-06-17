import time
class FastDictionary:
    def __init__(self):
        self._data = {}
    def add(self, key, value):
        self._data[key] = value
    def lookup(self, key):
        return self._data.get(key)
    def remove(self, key):
        if key in self._data:
            del self._data[key]
if __name__ == '__main__':
    d = FastDictionary()
    sample_data = {
        "user_001": {"id": 1, "name": "Alice", "email": "alice@example.com"},
        "user_002": {"id": 2, "name": "Bob", "email": "bob@example.com"},
        "product_A": {"sku": "P-001", "price": 99.99},
        "product_B": {"sku": "P-002", "price": 49.50}
    }
    for k, v in sample_data.items():
        d.add(k, v)
    start = time.time()
    results = [d.lookup(key) for key in ["user_001", "product_A"]]
    end = time.time()
    print(f"Lookup Results: {results}")
    print(f"Time taken: {end - start:.6f} seconds")