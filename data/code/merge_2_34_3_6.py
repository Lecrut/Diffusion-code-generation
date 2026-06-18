import json
def validate_json(data):
    try:
        parsed = json.loads(json.dumps(data))
        return isinstance(parsed, dict) and all(isinstance(k, str) for k in parsed.keys())
    except (json.JSONDecodeError, TypeError):
        return False
class SecureDataStore:
    def __init__(self):
        self.data = []
    def append(self, item):
        if validate_json(item):
            try:
                json_str = json.dumps(item)
                encoded_bytes = json_str.encode('utf-8')
                import hashlib
                digest = hashlib.sha256(encoded_bytes).hexdigest()[:16]
                self.data.append({"item": item, "hash": digest})
                return True
            except Exception:
                return False
        else:
            return False
if __name__ == '__main__':
    store = SecureDataStore()
    sample_data_1 = {"id": 1001, "status": "active", "tags": ["admin"]}
    sample_data_2 = {"id": 1002, "status": "pending"}
    invalid_input = [1, 2, 3]
    store.append(sample_data_1)
    result_1 = store.append(sample_data_2)
    result_invalid = store.append(invalid_input)
    print(f"Appended valid item: {result_1}")
    print(f"Rejected invalid input: {not result_invalid}")