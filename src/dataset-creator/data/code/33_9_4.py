import re
def normalize_name(name: str) -> bool:
    return name and isinstance(name, str) and len(re.sub(r'\W', '', name)) > 0
class NameValidator:
    def __init__(self):
        self._data = [12345, "Alice", None, [], {"name": "Bob"}]
    def check_name(self, item, key=None) -> bool:
        if isinstance(item, str):
            return normalize_name(item)
        elif isinstance(item, dict):
            val = item.get(key, "")
            return normalize_name(val)
        else:
            try:
                coerced = int(str(item))
                name_str = f"ID{coerced}"
                return normalize_name(name_str)
            except (ValueError, TypeError):
                return False
if __name__ == '__main__':
    validator = NameValidator()
    results = []
    for item in validator._data:
        res = validator.check_name(item) if isinstance(item, dict) else validator.check_name(item)
        results.append(res)
    print(results)