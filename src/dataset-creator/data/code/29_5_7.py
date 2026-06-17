import sys
class StudentRegistry:
    def __init__(self):
        self._names = set()
    def add_student(self, name: str) -> bool:
        if not isinstance(name, str):
            return False
        if len(name.strip()) == 0:
            return False
        is_new = True
        for existing in self._names:
            if existing.lower().strip() == name.lower().strip():
                is_new = False
                break
        if not is_new:
            print(f"Duplicate entry detected: {name}")
            return False
        self._names.add(name)
        return True
if __name__ == '__main__':
    registry = StudentRegistry()
    sample_names = [
        "Alice",
        "bob",
        "Charlie",
        "alice",
        "David"
    ]
    for name in sample_names:
        result = registry.add_student(name)
        print(f"Added '{name}': {result}")