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
            print(f"Duplicate entry detected for '{name}'.")
            return False
        else:
            self._names.add(name)
            print(f"Student '{name}' added successfully.")
            return True
    def get_count(self):
        return len(self._names)
if __name__ == '__main__':
    registry = StudentRegistry()
    sample_names = ["Alice", "Bob", "alice", "Charlie"]
    for name in sample_names:
        result = registry.add_student(name)
    print(f"Total unique students registered: {registry.get_count()}")