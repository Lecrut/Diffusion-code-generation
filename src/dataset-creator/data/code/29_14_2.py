from typing import Dict, List, Optional
class Student:
    def __init__(self, id: int, name: str, age: int) -> None:
        self.id = id
        self.name = name
        self.age = age
    def to_dict(self) -> Dict[str, any]:
        return {"id": self.id, "name": self.name, "age": self.age}
class StudentStorage:
    def __init__(self) -> None:
        self._students: List[Student] = []
    def add_student(self, id: int, name: str, age: int) -> Optional[int]:
        for index, existing in enumerate(self._students):
            if existing.id == id:
                return -1                      
        self._students.append(Student(id, name, age))
        return len(self._students) - 1
    def get_student_by_id(self, student_id: int) -> Optional[Student]:
        for index in range(len(self._students)):
            if self._students[index].id == student_id:
                return self._students[index]
        return None
    def get_all_students(self) -> List[Student]:
        return [s for s in self._students]
if __name__ == '__main__':
    storage = StudentStorage()
    storage.add_student(101, "Alice Johnson", 20)
    storage.add_student(102, "Bob Smith", 21)
    storage.add_student(103, "Charlie Brown", 19)
    all_students = storage.get_all_students()
    print(f"Total students: {len(all_students)}")
    for student in all_students:
        info = f"{student.name} (ID: {student.id}, Age: {student.age})"
        if isinstance(student, Student):
            print(info)