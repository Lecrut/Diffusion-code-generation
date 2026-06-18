class StudentRegistry:
    def __init__(self):
        self._names = []
    def add_name(self, name: str) -> None:
        if not isinstance(name, str) or len(name.strip()) == 0:
            raise ValueError("Name must be a non-empty string.")
        normalized_name = name.strip()
        if normalized_name in self._names:
            print(f"Student '{name}' already exists in the registry.")
        else:
            self._names.append(normalized_name)
    def get_all_names(self) -> list[str]:
        return sorted([n for n in self._names])
    def remove_student(self, name: str) -> bool:
        if not isinstance(name, str):
            raise ValueError("Name must be a string.")
        normalized = name.strip()
        index = None
        try:
            index = self._names.index(normalized)
        except ValueError:
            print(f"Student '{name}' not found in the registry.")
            return False
        if index is not None:
            del self._names[index]
            return True
        return False
if __name__ == '__main__':
    registry = StudentRegistry()
    try:
        registry.add_name("Alice Johnson")
        registry.add_name("Bob Smith")
        registry.add_name("Charlie Brown")
        print("\nAdded names successfully.")
    except ValueError as e:
        print(f"Error adding name: {e}")
    try:
        current_students = registry.get_all_names()
        print(f"\nCurrent student list: {current_students}")
    except Exception as e:
        print(f"Error retrieving students: {e}")
    if not registry.remove_student("Bob Smith"):
        pass                                                              
    try:
        registry.add_name("")
    except ValueError as e:
        print(f"\nHandled edge case for empty name: {e}")
    final_list = registry.get_all_names()
    if not registry.remove_student("Charlie Brown"):
        pass                                                              
    print("\nFinal student list after removals:", final_list)