class StudentManager:
    def __init__(self):
        self._students = []
    def add_student(self, name: str) -> None:
        if not isinstance(name, str):
            raise TypeError("Student name must be a string.")
        for student in self._students:
            if student.name == name:
                return
        new_student = Student(name=name)
        self._students.append(new_student)
    def get_all_students(self) -> list[str]:
        return [student.name for student in self._students]
class Student:
    __slots__ = ('name',)
    def __init__(self, name: str):
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        object.__setattr__(self, 'name', name)
if __name__ == '__main__':
    manager = StudentManager()
    manager.add_student('Alice')
    manager.add_student('Bob')
    manager.add_student('Charlie')
    print(manager.get_all_students())