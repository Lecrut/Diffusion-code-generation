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
        return sorted([n for n in self._names])
    def remove_entry(self, name: str) -> bool:
        if not isinstance(name, str):
            raise ValueError("Name must be a string.")
        normalized = name.strip()
        index = -1
        try:
            index = self._names.index(normalized)
        except ValueError:
            print(f"Entry '{name}' not found in registry.")
            return False
        del self._names[index]
        print(f"Successfully removed '{normalized}'.")
        return True
if __name__ == '__main__':
    registry = StudentRegistry()
    registry.add_name("Alice Johnson")
    registry.add_name("Bob Smith")
    registry.add_name("Charlie Brown")
    registry.add_name("Diana Prince")
    print("\n--- Current Registry ---")
    for name in registry.get_all_names():
        print(name)
    try:
        registry.add_name("Alice Johnson")
    except ValueError as e:
        pass
    result = registry.remove_entry("Bob Smith")
    if not result:
        print("\n--- Final Registry ---")
        for name in registry.get_all_names():
            print(name)