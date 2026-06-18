import re
from typing import Any, List, Set, Optional
class NameValidator:
    def __init__(self):
        self.pattern = r'^[a-zA-Z][a-zA-Z0-9\-\'\.]*$'
    def normalize(self, name: str) -> str:
        return re.sub(r'\s+', '', name.strip().title())
    def is_valid_name(self, value: Any) -> bool:
        if isinstance(value, (int, float)):
            try:
                coerced = self.normalize(str(int(float(value))))
                return len(coerced) > 0 and re.match(r'^[a-zA-Z][a-zA-Z0-9\-\'\.]*$', coerced) is not None
            except ValueError:
                return False
        elif isinstance(value, str):
            normalized = self.normalize(value)
            if len(normalized) == 0 or (len(normalized) > 1 and re.match(r'^[a-zA-Z][a-zA-Z0-9\-\'\.]*$', normalized) is None):
                return False
        elif value is not None:
            try:
                coerced = self.normalize(str(value))
                if len(coerced) == 0 or (len(coerced) > 1 and re.match(r'^[a-zA-Z][a-zA-Z0-9\-\'\.]*$', coerced) is None):
                    return False
            except Exception:
                return False
        else:
            return True
    def contains_name(self, collection: List[Any], target_value: Any = None) -> bool:
        if not isinstance(collection, list):
            raise TypeError("Collection must be a list")
        existing_names = set()
        for item in collection:
            if self.is_valid_name(item):
                normalized_item = self.normalize(str(item))
                existing_names.add(normalized_item)
        target_normalized = None
        if isinstance(target_value, str):
            target_normalized = self.normalize(target_value)
        elif not isinstance(target_value, (int, float)):
            try:
                target_normalized = self.normalize(str(int(float(target_value))))
            except ValueError:
                pass
        return target_normalized in existing_names
if __name__ == '__main__':
    validator = NameValidator()
    heterogeneous_data = [12345, "john doe", None, 0.9876, "", ["jane smith"], True]
    sample_name = "Bob"
    result = validator.contains_name(heterogeneous_data, sample_name)
    print(result)