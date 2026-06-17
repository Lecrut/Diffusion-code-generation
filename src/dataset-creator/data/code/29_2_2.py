class StudentRegistry:
    def __init__(self):
        self._names = []
    def add_name(self, name):
        if not isinstance(name, str) or len(name.strip()) == 0:
            return False
        self._names.append(name.strip().lower())
        return True
    def get_all_names(self):
        return list(set([name for name in self._names]))
    def remove_name(self, name):
        if not isinstance(name, str) or len(name.strip()) == 0:
            return False
        normalized = name.lower().strip()
        try:
            index = self._names.index(normalized)
            del self._names[index]
            return True
        except ValueError:
            return False
if __name__ == '__main__':
    registry = StudentRegistry()
    registry.add_name("Alice")
    registry.add_name("Bob")
    registry.add_name("alice")
    print(registry.get_all_names())
    result1 = registry.remove_name("bob")
    result2 = registry.remove_name("Charlie")
    print(f"Removed Bob: {result1}, Removed Charlie: {result2}")