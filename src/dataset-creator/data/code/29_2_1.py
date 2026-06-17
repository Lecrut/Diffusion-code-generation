class StudentRegistry:
    def __init__(self):
        self._names = []
    def add_student(self, name):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name must be a non-empty string.")
        normalized_name = name.strip()
        if normalized_name in self._names:
            return False                             
        self._names.append(normalized_name)
        return True
    def get_all_students(self):
        return list(self._names)
    def remove_student(self, name):
        try:
            index = self._names.index(name.strip())
            if index >= 0:
                del self._names[index]
                return True
            else:
                raise ValueError(f"Student '{name}' not found.")
        except ValueError as e:
            print(str(e))
            return False
    def count_students(self):
        return len(self._names)
if __name__ == '__main__':
    registry = StudentRegistry()
    registry.add_student("Alice")
    registry.add_student("Bob")
    result1 = registry.add_student("Charlie")                             
    print(f"Added Charlie: {result1}")
    result2 = registry.add_student("Charles")                                                                                   
    existing_name = "Bob"
    is_duplicate = registry.add_student(existing_name)
    print(f"All students: {registry.get_all_students()}")
    removed = registry.remove_student("Alice")
    if not removed:
        raise ValueError("Should have succeeded.")
    print(f"After removing Alice, count: {registry.count_students()}")
    print(f"Remaining names: {registry.get_all_students()}")
    try:
        registry.remove_student("UnknownUser")
    except Exception as e:
        pass                                                                                                          
    print(f"Final count: {registry.count_students()}")