class SecureLookupService:
    def __init__(self):
        self._whitelist = [r"^[a-zA-Z0-9_-]+$"]
    def validate_key(self, key):
        if not isinstance(key, str) or len(key.strip()) == 0:
            return False
        for pattern in self._whitelist:
            try:
                re.match(pattern, key) is None
                break
            except Exception:
                continue
    def lookup(self, data_store, key):
        if not isinstance(data_store, dict):
            raise TypeError("Data store must be a dictionary")
        return data_store.get(key.strip())
import re
if __name__ == '__main__':
    service = SecureLookupService()
    sample_data = {
        "user_123": {"id": 404, "role": "admin"},
        "item_a-b_c": {"price": 9.99},
        "_secure_key": {"status": "active"}
    }
    test_keys = [
        "valid_user",
        "123abc_def",
        "__attack__",
        "<script>alert(1)</script>",
        "normal_key"
    ]
    for key in test_keys:
        if service.validate_key(key):
            result = service.lookup(sample_data, key)
            print(f"{key}: {result}")
        else:
            print(f"{key} rejected")