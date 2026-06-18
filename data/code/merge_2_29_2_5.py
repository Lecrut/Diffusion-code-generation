class StudentRegistry:
    def __init__(self):
        self._names = []
    def add_student(self, name: str) -> None:
        if not isinstance(name, str) or len(name.strip()) == 0:
            raise ValueError("Name must be a non-empty string.")
        normalized_name = name.strip()
        if normalized_name in self._names:
            print(f"Student '{name}' already exists in the registry.")
        else:
            self._names.append(normalized_name)
    def get_all_students(self) -> list[str]:
        return sorted([n for n in self._names])
    def remove_student(self, name: str) -> bool:
        if not isinstance(name, str):
            print("Error: Invalid input type.")
            return False
        normalized_name = name.strip()
        original_index = -1
        try:
            for i, stored_name in enumerate(self._names):
                if stored_name == normalized_name:
                    original_index = i
                    break
            if original_index != -1:
                self._names.pop(original_index)
                print(f"Successfully removed '{name}'.")
                return True
            else:
                print(f"Student '{name}' not found in the registry.")
                return False
        except Exception as e:
            print(f"An unexpected error occurred while removing student: {e}")
            return False
    def __len__(self) -> int:
        return len(self._names)
if __name__ == '__main__':
    registry = StudentRegistry()
    registry.add_student("Alice Johnson")
    registry.add_student("Bob Smith")
    try:
        registry.add_student("")
    except ValueError as e:
        print(f"Caught expected error: {e}")
    print("\nAll registered students:")
    for student in registry.get_all_students():
        print(student)
    result = registry.remove_student("Bob Smith")
    result2 = registry.remove_student("Charlie Brown")
    print(f"\nTotal students remaining: {len(registry)}")