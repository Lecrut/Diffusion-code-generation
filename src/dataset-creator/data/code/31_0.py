import time
class FastDictionary:
    def __init__(self):
        self._data = {}
    def lookup(self, key):
        return self._data.get(key)
    def add_entry(self, key, value):
        self._data[key] = value
if __name__ == '__main__':
    d = FastDictionary()
    sample_data = {
        "user_001": {"id": 1, "role": "admin"},
        "user_002": {"id": 2, "role": "editor"},
        "product_A": {"sku": "P-987", "price": 45.99},
        "order_XYZ": {"status": "shipped", "date": "2023-10-01"}
    }
    for k, v in sample_data.items():
        d.add_entry(k, v)
    start = time.perf_counter()
    results = [d.lookup(key) for key in ["user_001", "product_A"]]
    end = time.perf_counter()
    print("Lookup Results:", results)
    print(f"Execution Time: {end - start:.6f} seconds")