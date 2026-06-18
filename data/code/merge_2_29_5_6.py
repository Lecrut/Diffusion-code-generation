import sys
class StudentRegistry:
    def __init__(self):
        self._names = set()
    def add_student(self, name: str) -> bool:
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        return self._names.add(name) is None
def main():
    registry = StudentRegistry()
    sample_names = ["Alice", "Bob", "Charlie", "David"]
    for name in sample_names:
        result = registry.add_student(name)
        if not result:
            print(f"Duplicate detected: {name}")
        else:
            print(f"Added successfully: {name}")
if __name__ == '__main__':
    main()