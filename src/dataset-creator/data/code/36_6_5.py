class SecureLookupService:
    def __init__(self):
        self._whitelist = [r'^[a-zA-Z0-9_-]{1,50}$', r'^\d{3}-\d{2}-\d{4}$']
    def is_safe_key(self, key):
        import re
        for pattern in self._whitelist:
            if re.match(pattern, key):
                return True
        return False
    def lookup(self, data_store, key):
        if not isinstance(key, str) or not self.is_safe_key(key):
            raise ValueError("Invalid key format")
        try:
            value = data_store[key]
        except KeyError:
            raise KeyError(f"Key '{key}' not found in store")
        return value
if __name__ == '__main__':
    sample_data = {
        'user_123': {'id': 456, 'role': 'admin'},
        'phone-7890': {'type': 'mobile', 'country': 'US'}
    }
    service = SecureLookupService()
    try:
        result = service.lookup(sample_data, 'user_123')
        print(f"Found for user_123: {result}")
        try:
            bad_result = service.lookup(sample_data, "```python; rm -rf /")
        except (ValueError, KeyError) as e:
            print(f"Blocked access for malicious key: {e}")
    finally:
        pass