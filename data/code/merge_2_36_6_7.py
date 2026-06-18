import re
class SecureLookupService:
    def __init__(self):
        self.whitelist_patterns = [r'^[a-zA-Z0-9_-]{3}$', r'^ID-\d{4}$']
    def validate_key(self, key):
        if not isinstance(key, str) or len(key.strip()) == 0:
            return False
        for pattern in self.whitelist_patterns:
            if re.match(pattern, key.strip()):
                return True
        return False
    def lookup(self, data_store, key):
        if not self.validate_key(key):
            raise ValueError("Invalid or unauthorized key detected")
        normalized_key = key.strip()
        return data_store.get(normalized_key)
if __name__ == '__main__':
    sample_data = {
        "user-123": {"id": 405, "role": "admin"},
        "ID-9876": {"id": 406, "status": "active"}
    }
    service = SecureLookupService()
    try:
        result = service.lookup(sample_data, "user-123")
        print(f"Found: {result}")
        malicious_key = "<script>alert('xss')</script>"
        if not service.validate_key(malicious_key):
            print("Injection attempt blocked.")
    except ValueError as e:
        print(f"Error: {e}")