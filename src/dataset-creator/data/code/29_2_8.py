class StudentRegistry:
    def __init__(self):
        self._names = []
    def add_name(self, name: str) -> None:
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        stripped_name = name.strip()
        if not stripped_name:
            return
        if stripped_name in self._names:
            print(f"Student '{stripped_name}' already exists.")
        else:
            self._names.append(stripped_name)
    def get_all_names(self) -> list[str]:
        return sorted(list(set(self._names)))
    def remove_student(self, name: str) -> bool:
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        stripped = name.strip()
        exists = False
        for i, student in enumerate(self._names):
            if student == stripped:
                self._names.pop(i)
                return True
        print(f"Student '{stripped}' not found.")
        return False
if __name__ == '__main__':
    registry = StudentRegistry()
    sample_names = ["Alice", "  Bob ", "", "Charlie"]
    for name in sample_names:
        try:
            registry.add_name(name)
        except TypeError as e:
            print(f"Error adding {name}: {e}")
    all_students = registry.get_all_names()
    print("Current students:", all_students)
    remove_target = "Bob"
    if registry.remove_student(remove_target):
        print(f"{remove_target} removed successfully.")
    remaining = registry.get_all_names()
    print("Remaining students:", remaining)