import re
def normalize_name(name: str) -> bool:
    return name and all(c.isalpha() for c in name.strip())
class NameValidator:
    def __init__(self):
        self._names = set()
    def add(self, item):
        if isinstance(item, (str, int)):
            val = str(item).strip().lower()
            if normalize_name(val) and not any(n.lower() == val for n in self._names):
                self._names.add(val)
        elif hasattr(item, '__iter__') and not isinstance(item, str):
            for i in item:
                try:
                    self.add(i)
                except Exception:
                    pass
    def contains(self, name: any) -> bool:
        if normalize_name(str(name)):
            return any(n.lower() == str(name).strip().lower() for n in self._names)
        return False
if __name__ == '__main__':
    validator = NameValidator()
    validator.add("Alice")
    validator.add(1234567890)
    validator.add(["Bob", "charlie"])
    print(validator.contains("alice"))        
    print(validator.contains("bob"))         
    print(validator.contains("david"))