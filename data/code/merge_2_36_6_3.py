import re
class SecureLookupService:
    def __init__(self):
        self.whitelist_patterns = [
            r'^[a-zA-Z0-9_-]+$',                                           
            r'^(25)[0-5]{1}$',                            
        ]
    def is_safe_key(self, key: str) -> bool:
        if not isinstance(key, str):
            return False
        for pattern in self.whitelist_patterns:
            if re.match(pattern, key):
                return True
        return False
if __name__ == '__main__':
    service = SecureLookupService()
    test_keys = [
        "valid_user_123",
        "abc-xyz789",
        "<script>alert('xss')</script>",
        "\"', --;",
        "normal_key",
        "key with space"
    ]
    for key in test_keys:
        status = "SAFE" if service.is_safe_key(key) else "INJECTED"
        print(f"{status}: {repr(key)}")