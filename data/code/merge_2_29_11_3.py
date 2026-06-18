import sys
class StudentRecord:
    def __init__(self, name):
        self._name = name
    @property
    def name(self):
        return self._name
class StudentManager:
    def __init__(self):
        self._students = []
    def add_student(self, student_record: StudentRecord) -> None:
        if not isinstance(student_record, StudentRecord):
            raise TypeError("Invalid record type")
        self._students.append(student_record)
    def get_all_names(self) -> list[str]:
        return [student.name for student in self._students]
if __name__ == '__main__':
    manager = StudentManager()
    records = [StudentRecord(f"Student_{i}") for i in range(1, 5)]
    for record in records:
        manager.add_student(record)
    names = manager.get_all_names()
    print("Names:", ", ".join(names))