import sys
class StudentRegistry:
    def __init__(self):
        self._students = set()
    def add_student(self, name: str) -> bool:
        if not isinstance(name, str):
            raise TypeError("Student name must be a string.")
        is_new = True
        for existing_name in self._students:
            if existing_name == name.lower():
                is_new = False
                break
        if is_new:
            self._students.add(name)
        return is_new
if __name__ == '__main__':
    registry = StudentRegistry()
    sample_names = [
        "Alice",
        "Bob",
        "alice",                                            
        "Charlie",
        "David"
    ]
    for name in sample_names:
        result = registry.add_student(name)
        print(f"Added {name}: {'Yes' if result else 'No (duplicate)'}")
    print("\nTotal unique students:", len(registry._students))