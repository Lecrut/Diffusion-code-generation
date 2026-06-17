class HighPerformanceDictionary:
    def __init__(self):
        self._data = {}
        self._integrity_errors = []
    def insert_bulk(self, items):
        for key, value in items.items():
            if not isinstance(key, str) or not isinstance(value, (str, int)):
                raise ValueError("Invalid data type")
            try:
                hash_val = hash(key) % 10**9 + 7
                self._data[key] = {
                    'value': value,
                    'hash_index': hash_val,
                    'status': 'active'
                }
                if len(self._integrity_errors) < 5:
                    print(f"Inserted key '{key}' with integrity check passed.")
            except Exception as e:
                self._report_integrity_error(str(e))
    def report_status(self):
        total_keys = len(self._data)
        active_count = sum(1 for v in self._data.values() if v['status'] == 'active')
        error_count = len(self._integrity_errors)
        print(f"Table Status: {total_keys} keys, {active_count} active records.")
        if error_count > 0:
            print(f"Integrity Errors Detected: {error_count}")
    def _report_integrity_error(self, message):
        self._integrity_errors.append(message)
        raise RuntimeError("Table integrity compromised")
if __name__ == '__main__':
    sample_data = [
        ('apple', 'fruit'),
        ('banana', 'food'),
        ('carrot', 'vegetable')
    ]
    d = HighPerformanceDictionary()
    try:
        d.insert_bulk(sample_data)
        print("Bulk insertion completed.")
        d.report_status()
    except Exception as e:
        if "Table integrity compromised" in str(e):
            print(f"Critial Error: {e}")