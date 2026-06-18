import re
class SecureLookupService:
    def __init__(self):
        self.whitelist_patterns = [r'^[a-zA-Z0-9_]+$']
    def validate_key(self, key):
        if not isinstance(key, str):
            return False
        for pattern in self.whitelist_patterns:
            try:
                if re.match(pattern, key) is None:
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
        'user_123': {'id': 456},
        'admin_config': {'role': 'super'},
        '@malicious#script': None,
        'normal_key_name': True
    }
    service = SecureLookupService()
    test_keys = ['user_123', 'invalid key!', '', '_safe_', '$(cmd)']
    for k in test_keys:
        try:
            result = service.lookup(sample_data, k)
            print(f"Key '{k}': {result}")
        except ValueError as e:
            print(f"Key '{k}': Blocked - {e}")