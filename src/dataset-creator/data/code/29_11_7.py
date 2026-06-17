import sys
class StudentRecord:
    def __init__(self):
        self._names = []
    @property
    def names(self) -> list[str]:
        return [n for n in reversed(self._names)]
    @names.setter
    def names(self, value: list[str]):
        if isinstance(value, (list, tuple)):
            self._names.extend([str(n) for n in value])
class StudentManager:
    def __init__(self):
        self.students = {}
    def add_student(self, name: str, student_id: int | None = None):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        id_to_use = student_id or len(self.students) + 1
        record = StudentRecord()
        record.names.append(name)
        self.students[id_to_use] = {
            "id": id_to_use,
            "name": name,
            "_record_obj": record
        }
    def get_student_by_id(self, student_id: int | None = None):
        if not isinstance(student_id, (int, str)):
            raise TypeError("Student ID must be an integer")
        id_to_check = int(student_id)
        return self.students.get(id_to_check)
if __name__ == '__main__':
    manager = StudentManager()
    sample_students = [
        ("Alice Johnson", 1),
        ("Bob Smith", None),
        ("Charlie Brown", "3"),
        ("Diana Prince", 4),
        ("Ethan Hunt", None)
    ]
    for name, sid in sample_students:
        manager.add_student(name=name, student_id=sid)
    print(f"Total students managed: {len(manager.students)}")
    all_names_valid = True
    for s_data in manager.students.values():
        if not isinstance(s_data["_record_obj"].names, list):
            all_names_valid = False
    print(f"Data integrity check passed: {all_names_valid}")