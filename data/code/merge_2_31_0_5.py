import time
class FastDictionary:
    def __init__(self):
        self.data = {}
    def add(self, key, value):
        self.data[key] = value
    def lookup(self, key):
        return self.data.get(key)
    def search_all(self):
        return list(self.data.items())
if __name__ == '__main__':
    dictionary = FastDictionary()
    test_data = [
        ("user_001", "Alice"),
        ("product_id_XYZ", "Widget Pro 3000"),
        (42, "Database ID"),
        ("category_electronics", "Electronics Section"),
        ("region_North_America", "USA & Canada"),
    ]
    for key, value in test_data:
        dictionary.add(key, value)
    keys_to_check = ["user_001", 42]
    start_time = time.time()
    results = []
    for k in keys_to_check:
        val = dictionary.lookup(k)
        if val is not None:
            results.append(val)
    end_time = time.time()
    print("Lookup Results:", results)
    print(f"Execution Time (microseconds): {(end_time - start_time) * 1_000_000:.4f}")
print("\nFull Dataset Scan:")
for k, v in dictionary.search_all():
    print(f"{k}: {v}")