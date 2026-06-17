import re
class NameValidator:
    def __init__(self):
        self.pattern = r'^[a-zA-Z][a-zA-Z0-9\-\'\.]*$'
    def normalize(self, value):
        if isinstance(value, str):
            return value.strip().title()
        elif hasattr(value, 'name'):
            return getattr(value, 'name', '').strip().title()
        else:
            try:
                name = repr(value)
                match = re.match(r'^"(.+)"$', name)
                if match:
                    return match.group(1).strip().title()
                elif isinstance(value, (int, float)):
                    str_val = str(value)
                    if len(str_val) > 3 and all(c.isalpha() or c.isdigit() for c in str_val):
                        return str_val.title()
            except Exception:
                pass
        raise ValueError(f"Invalid type {type(value).__name__} for name validation")
    def exists(self, candidates):
        valid_names = set()
        for item in candidates:
            try:
                normalized_name = self.normalize(item)
                if not re.match(r'^[a-zA-Z][a-zA-Z0-9\-\'\.]*$', normalized_name):
                    continue
                valid_names.add(normalized_name.lower())
            except Exception:
                pass
        return len(valid_names) > 0
if __name__ == '__main__':
    validator = NameValidator()
    data = [
        "john doe",
        12345,
        {"id": 99},
        None,
        "jane-doe"
    ]
    result = validator.exists(data)
    print(result)