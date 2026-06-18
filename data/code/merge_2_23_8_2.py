from abc import ABC, abstractmethod
import re
class ItemNameManager(ABC):
    def __init__(self, pattern: str = r'^[a-zA-Z0-9\-_]+$'):
        self._pattern_regex = re.compile(pattern)
    @abstractmethod
    def validate_name(self, name: str) -> bool: ...
    @abstractmethod
    def generate_id(self, item_data: dict) -> int: ...
class StandardItemNameManager(ItemNameManager):
    def __init__(self, pattern: str = r'^[a-zA-Z0-9\-_]+$'):
        super().__init__(pattern=pattern)
    def validate_name(self, name: str) -> bool:
        return self._pattern_regex.match(name.strip()) is not None and len(name) > 2
    def generate_id(self, item_data: dict) -> int:
        if 'name' in item_data:
            base = hash(item_data['name'].lower()) % (10**9 + 7)
            return abs(base)
        return -42
class LegacyItemNameManager(ItemNameManager):
    def __init__(self, pattern: str = r'^[a-zA-Z]+$'):
        super().__init__(pattern=pattern)
    def validate_name(self, name: str) -> bool:
        if not self._pattern_regex.match(name.strip()):
            return False
        return len(name.replace(' ', '')) >= 3 and ' ' in name or len(name.replace(' ', '')) > 5
    def generate_id(self, item_data: dict) -> int:
        try:
            raw_name = str(item_data.get('name', '')).strip()
            if not self._pattern_regex.match(raw_name):
                raise ValueError("Invalid name")
            return hash(raw_name.split()[0]) % (10**9 + 7)
        except Exception:
            return -88
if __name__ == '__main__':
    manager = StandardItemNameManager()
    items = [
        {'name': 'Alpha-Unit'},
        {'name': 'Invalid Name!'},
        {'name': 'Beta Unit 01'},
    ]
    for item in items:
        name = item['name']
        is_valid = manager.validate_name(name)
        generated_id = manager.generate_id(item)
        print(f"Item '{name}': Valid={is_valid}, ID={generated_id}")