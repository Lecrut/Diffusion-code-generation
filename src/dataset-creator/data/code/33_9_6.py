import re
class NameValidator:
    def __init__(self):
        self.pattern = r'^[a-zA-Z][a-zA-Z0-9\-\'\.]{1,30}$'
    def normalize(self, name):
        if not isinstance(name, str):
            try:
                name = str(name)
            except Exception:
                return None
        name = re.sub(r'\s+', ' ', name).strip()
        if len(name) == 0 or any(ord(c) > 127 for c in name[:3]):
            return None
        return name
    def validate(self, candidate):
        normalized = self.normalize(candidate)
        if not isinstance(normalized, str):
            return False
        if re.match(r'^[a-zA-Z][a-zA-Z0-9\-\'\.]*$', normalized) is None:
            return False
        return True
class NameDatabase:
    def __init__(self):
        self._data = {}
    def add(self, key, value):
        if not isinstance(key, (str, int)):
            raise TypeError("Key must be string or integer")
        normalized_key = str(key).strip().lower() if isinstance(key, str) else f"key_{int(key)}"
        self._data[normalized_key] = value
    def exists(self, candidate):
        return candidate in self._data
if __name__ == '__main__':
    validator = NameValidator()
    db = NameDatabase()
    raw_entries = [
        ("John Doe", "Valid"),
        (12345, "Numeric ID"),
        ("Ana-María García-Andrés", "Special chars"),
        ("invalid name!", "Invalid start")
    ]
    for entry in raw_entries:
        if len(entry) == 2:
            key_str = str(entry[0])
            value = entry[1]
            normalized_key = validator.normalize(key_str)
            db.add(normalized_key, value)
        test_cases = [entry[0], "TestUser", None, True]
        for tc in test_cases:
            if not isinstance(tc, str):
                try:
                    tc = str(tc).strip()
                except Exception:
                    continue
            is_valid = validator.validate(tc)
            exists = db.exists(tc.lower())
            print(f"Input: {tc!r} | Validated: {is_valid} | Exists in DB: {exists}")
    sample_check = "John Doe".lower()
    if db.exists(sample_check):
        print("Sample check passed.")