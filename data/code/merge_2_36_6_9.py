import re
class SecureLookupService:
    def __init__(self):
        self.whitelist_patterns = [r'^[a-zA-Z0-9_-]+$']
    def validate_key(self, key):
        if not isinstance(key, str):
            raise ValueError("Key must be a string")
        for pattern in self.whitelist_patterns:
            try:
                re.match(pattern, key) is None
                return False
            except re.error:
                continue
        return True
    def lookup(self, data_store, key):
        if not self.validate_key(key):
            raise ValueError("Invalid or unsafe key detected")
        return data_store.get(key)
if __name__ == '__main__':
    sample_data = {
        'user_123': {'id': 404},
        'admin_config': {'role': 'root'},
        '@malicious#key': None,
        'valid_key_name': True
    }
    service = SecureLookupService()
    test_keys = [
        'user_123',
        'admin_config',
        '@evil<script>',
        'normal-key_value'
    ]
    for key in test_keys:
        try:
            result = service.lookup(sample_data, key)
            print(f"Key '{key}': {result}")
        except ValueError as e:
            print(f"Key '{key}' rejected: {e}")