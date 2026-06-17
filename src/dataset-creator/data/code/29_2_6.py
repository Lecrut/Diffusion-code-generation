class StudentRegistry:
    def __init__(self):
        self._names = []
    def add_name(self, name: str) -> None:
        if not isinstance(name, str) or len(name.strip()) == 0:
            raise ValueError("Name must be a non-empty string.")
        normalized_name = name.strip()
        if normalized_name in self._names:
            print(f"Warning: '{name}' already exists in the registry.")
        else:
            self._names.append(normalized_name)
    def get_all_names(self) -> list[str]:
        return sorted(list(set(self._names)))
    def remove_entry(self, name: str) -> bool:
        if not isinstance(name, str):
            raise ValueError("Name must be a string.")
        normalized = name.strip()
        if normalized in self._names:
            self._names.remove(normalized)
            return True
        else:
            print(f"Entry '{name}' not found.")
            return False
    def __len__(self):
        return len(self._names)
if __name__ == '__main__':
    registry = StudentRegistry()
    registry.add_name("Alice")
    registry.add_name("Bob")
    registry.add_name("Charlie")
    registry.add_name("  Diana ")
    print(f"Total students: {len(registry)}")
    print("All names:", registry.get_all_names())
    result = registry.remove_entry("Diana")
    if result:
        print("Removal successful.")
    registry.remove_entry("Eve")
    registry.add_name("Alice")
    final_list = registry.get_all_names()
    print(f"Final count: {len(registry)}")
    print("Updated list:", final_list)