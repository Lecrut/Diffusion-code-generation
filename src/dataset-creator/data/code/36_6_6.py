import re
class SecureLookupService:
    def __init__(self):
        self._allowed_patterns = [r'^[a-zA-Z0-9_]+$']
    def validate_key(self, key):
        for pattern in self._allowed_patterns:
            if not isinstance(key, str) or re.match(pattern, key):
                return True
        raise ValueError(f"Invalid key format: {key}")
    def lookup(self, data_store, key):
        try:
            self.validate_key(key)
            return data_store.get(key)
        except (ValueError, KeyError):
            raise
if __name__ == '__main__':
    sample_data = {'admin_panel': 'Secure Mode', 'user_123': 'Active'}
    service = SecureLookupService()
    try:
        result = service.lookup(sample_data, "valid_key")
        print(f"Success for valid key (simulated): {result}")
        malicious_input = "user; DROP TABLE users;"
        try:
            service.lookup(sample_data, malicious_input)
        except ValueError as e:
            print(f"Injection blocked: {e}")
    except Exception as ex:
        if 'Invalid key format' in str(ex):
            pass