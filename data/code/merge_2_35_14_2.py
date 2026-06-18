class EfficientLookup:
    def __init__(self, data: dict) -> None:
        self.data = data if isinstance(data, dict) else {}
    def find_element(self, key, value=None) -> bool:
        try:
            return key in self.data and (value is None or self.data[key] == value)
        except Exception:
            return False
    def get_value(self, key, default=None):
        try:
            return self.data[key] if key in self.data else default
        except Exception:
            return default
if __name__ == '__main__':
    sample_data = {
        "user_id": 101,
        "username": "alice",
        "email": "alice@example.com"
    }
    efficient_lookup = EfficientLookup(sample_data)
    result_key_only = efficient_lookup.find_element("user_id")
    result_exact_match = efficient_lookup.find_element("username", "alice")
    print(f"Key 'user_id' exists: {result_key_only}")
    print(f"Exact match for username='alice': {result_exact_match}")
    retrieved_name = efficient_lookup.get_value("email", "unknown@example.com")
    missing_key_result = efficient_lookup.get_value("phone_number", "+1-555-0000")
    print(f"Retrieved email (safe): {retrieved_name}")
    print(f"Missing phone number result: {missing_key_result}")