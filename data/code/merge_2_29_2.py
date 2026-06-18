class StudentRegistry:
    def __init__(self):
        self._names = []
    def add_student(self, name: str) -> None:
        if not isinstance(name, str) or len(name.strip()) == 0:
            raise ValueError("Name must be a non-empty string.")
        normalized_name = name.strip()
        if normalized_name in self._names:
            print(f"Student '{normalized_name}' already exists.")
        else:
            self._names.append(normalized_name)
    def get_all_students(self) -> list[str]:
        return sorted(list(set(self._names)))
    def remove_student(self, name: str) -> bool:
        if not isinstance(name, str):
            print("Invalid input type.")
            return False
        normalized_name = name.strip()
        try:
            index = self._names.index(normalized_name)
            removed = self._names.pop(index)
            print(f"Removed student '{removed}'.")
            return True
        except ValueError:
            print(f"Student '{normalized_name}' not found.")
            return False
    def __str__(self):
        return f"{len(self.get_all_students())} students registered."
if __name__ == '__main__':
    registry = StudentRegistry()
    registry.add_student("Alice Johnson")
    registry.add_student("Bob Smith")
    registry.add_student("Charlie Brown")
    registry.add_student("David Lee")
    print("\nAll students:")
    for student in registry.get_all_students():
        print(f"  - {student}")
    result = registry.remove_student("Alice Johnson")
    if not result:
        registry.remove_student("Unknown User")
    print("\nFinal count:", str(registry))