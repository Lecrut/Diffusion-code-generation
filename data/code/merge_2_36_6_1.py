import re
class SecureLookupService:
    def __init__(self):
        self.whitelist_patterns = [r'^[a-zA-Z0-9_-]{3}$']                             
    def is_safe_key(self, key):
        for pattern in self.whitelist_patterns:
            if re.match(pattern, key):
                return True
        return False
if __name__ == '__main__':
    service = SecureLookupService()
    safe_keys = ['abc', 'xyz123']
    unsafe_keys = ['<script>', "key\"'"]
    print("Safe keys:", [k for k in safe_keys if service.is_safe_key(k)])
    print("Unsafe keys blocked:", all(not service.is_safe_key(k) for k in unsafe_keys))