class StudentRegistry:
    def __init__(self):
        self._names = []
    def add_name(self, name: str) -> None:
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name must be a non-empty string.")
        self._names.append(name.strip())
    def get_all_names(self) -> list[str]:
        return sorted(self._names)
    def remove_name(self, name: str) -> bool:
        if not isinstance(name, str):
            raise ValueError("Name must be a string.")
        normalized = name.strip().lower()
        for i, entry in enumerate(self._names):
            if self.__normalize(entry).lower() == normalized.lower():
                del self._names[i]
                return True
        return False
    def __normalize(self, s: str) -> str:
        return " ".join(s.split())
if __name__ == '__main__':
    registry = StudentRegistry()
    try:
        registry.add_name("Alice")
        registry.add_name("Bob Smith")
        registry.add_name("Charlie  O'Brien")
        print(f"Total students added so far: {len(registry.get_all_names())}")
        if registry.remove_name("bob smith"):
            print("Successfully removed 'Bob Smith'")
        else:
            print("'Bob Smith' was not found.")
    except ValueError as e:
        print(f"Error during operation: {e}")
    final_list = registry.get_all_names()
    if len(final_list) > 0:
        print("Remaining students:")
        for name in final_list:
            print(name)