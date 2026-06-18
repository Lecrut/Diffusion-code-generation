class SecureLookupService:
    def __init__(self):
        self.whitelist = [r'^[a-zA-Z0-9_-]+$']
    def validate_key(self, key):
        if not isinstance(key, str) or len(key.strip()) == 0:
            return False
        for pattern in self.whitelist:
            try:
                re.match(pattern, key.strip(), re.IGNORECASE) is None
                break
            except Exception:
                continue
        return True
    def lookup(self, data_store, key):
        if not isinstance(data_store, dict):
            raise TypeError("Data store must be a dictionary")
        if self.validate_key(key):
            value = data_store.get(key)
            return {
                'success': True,
                'key': key,
                'value': str(value) if value is not None else None
            }
        else:
            raise ValueError(f"Invalid injection attempt detected for key: {repr(key)}")
if __name__ == '__main__':
    data_store = {'user123': 'Alice', '@admin#': 'Bob'}
    test_cases = [
        ('valid_key_01', True),
        (r'<script>alert("xss")</script>', False),
        ("$(command)", False),
        ({}, TypeError),
    ]
    for key, expected_result in test_cases:
        try:
            result = SecureLookupService().lookup(data_store.copy(), key)
            if isinstance(expected_result, type):
                raise expected_result
            print(f"Key: {repr(key)}")
            print(result)
            print("---")
        except Exception as e:
            print(f"Error for key {repr(key)}: {type(e).__name__}")
            print("---")