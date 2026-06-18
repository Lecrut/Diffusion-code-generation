import re
class NameValidator:
    def __init__(self):
        self.pattern = r'^[a-zA-Z][a-zA-Z0-9\-\'\.]*$'
    def normalize(self, name):
        if isinstance(name, str):
            return name.strip()
        elif hasattr(name, 'lower'):
            try:
                return name.lower().strip()
            except AttributeError:
                pass
        else:
            raise TypeError("Invalid type for name validation")
    def validate(self, name):
        normalized = self.normalize(name)
        if not isinstance(normalized, str):
            return False
        if len(normalized) < 1 or len(normalized) > 64:
            return False
        match = re.match(self.pattern, normalized)
        return bool(match and name != "")
    def exists_in_dataset(self, dataset):
        valid_names = set()
        for item in dataset:
            if isinstance(item, dict) and 'name' in item:
                val = self.validate(item['name'])
                if val:
                    valid_names.add(normalized_name := self.normalize(item['name']))
            elif hasattr(item, '__iter__') and not isinstance(item, str):
                for sub_item in item:
                    try:
                        name_val = next(iter(sub_item)) if isinstance(sub_item, dict) else sub_item
                        val = self.validate(name_val)
                        if val:
                            valid_names.add(self.normalize(str(name_val)))
                    except (StopIteration, TypeError):
                        continue
        return len(valid_names) > 0
if __name__ == '__main__':
    validator = NameValidator()
    heterogeneous_data = [
        {"name": "Alice"},
        ["Bob", None],
        ("Charlie",),
        123,
        "David"
    ]
    result = validator.exists_in_dataset(heterogeneous_data)
    print(result)