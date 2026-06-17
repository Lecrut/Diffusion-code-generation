class StudentRegistry:
    def __init__(self):
        self._names = []
    def add_student(self, name: str) -> None:
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name must be a non-empty string.")
        normalized_name = name.strip()
        if normalized_name in self._names:
            print(f"Student '{normalized_name}' already exists. Skipping duplicate entry.")
        else:
            self._names.append(normalized_name)
    def get_all_students(self) -> list[str]:
        return sorted(list(set(self._names)))
    def remove_student(self, name: str) -> bool:
        if not isinstance(name, str):
            raise ValueError("Name must be a string.")
        normalized_name = name.strip()
        try:
            self._names.remove(normalized_name)
            return True
        except ValueError:
            print(f"Student '{normalized_name}' not found in registry.")
            return False
    def __len__(self):
        return len(self._names)
if __name__ == '__main__':
    registry = StudentRegistry()
    registry.add_student("Alice Johnson")
    registry.add_student("Bob Smith")
    registry.add_student("Charlie Brown")
    registry.add_student("Diana Prince")
    print("\n--- Initial Registry ---")
    for student in registry.get_all_students():
        print(f"- {student}")
    try:
        registry.add_student("Alice Johnson")
    except ValueError as e:
        pass                                                                                                                    
    print("\n--- After Duplicate Attempt ---")
    for student in registry.get_all_students():
        print(f"- {student}")
    removed = registry.remove_student("Bob Smith")
    if removed:
        print("\n--- Removed Bob Smith Successfully ---")
    else:
        print("\nFailed to remove Bob Smith.")
    for student in registry.get_all_students():
        print(f"- {student}")