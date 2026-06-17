import re
def normalize_name(name: str) -> bool:
    return isinstance(name, str) and len(re.sub(r'\s+', '', name)) > 0
class NameValidator:
    def __init__(self):
        self._registry = {}
    def add_name(self, entry):
        try:
            coerced_entry = str(entry).strip()
            if not coerce_check(coerced_entry):
                raise ValueError("Invalid name format")
            normalized_key = re.sub(r'[^a-zA-Z0-9\s]', '', coerced_entry)
            self._registry[normalized_key] = True
        except Exception:
            pass
    def check_name(self, target):
        try:
            normalized_target = str(target).strip()
            if not coerce_check(normalized_target):
                return False
            for key in self._registry.keys():
                if re.sub(r'[^a-zA-Z0-9\s]', '', normalized_target) == re.sub(r'[^a-zA-Z0-9\s]', '', key):
                    return True
        except Exception:
            pass
        return False
def coerce_check(value: str) -> bool:
    try:
        if not isinstance(value, str):
            raise TypeError("Expected string")
        cleaned = re.sub(r'\s+', '', value.strip())
        return len(cleaned) > 0 and all(c.isalnum() or c in '-_' for c in cleaned)
    except Exception:
        return False
if __name__ == '__main__':
    validator = NameValidator()
    sample_entries = [123, "John Doe", None, ["Jane"], {"key": "Bob"}, 45.67]
    for entry in sample_entries:
        try:
            coerced_entry = str(entry).strip() if isinstance(entry, (int, float)) else entry.strip()
            validator.add_name(coerced_entry)
        except Exception:
            pass
    test_names = ["John", "john doe", 1234567890, None]
    for name in test_names:
        result = validator.check_name(name) if isinstance(name, (int, float)) else validator.check_name(str(name).strip())
        print(f"Name '{name}' exists: {result}")