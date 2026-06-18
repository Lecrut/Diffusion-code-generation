from typing import List, Dict
class Student:
    def __init__(self, id_number: str, first_name: str, last_name: str, grade_level: int) -> None:
        self.id = id_number
        self.first_name = first_name
        self.last_name = last_name
        self.grade_level = grade_level
class StudentStorageSystem:
    def __init__(self, capacity: int) -> None:
        if capacity <= 0:
            raise ValueError("Capacity must be greater than zero.")
        self._capacity = capacity
        self._students: List[Student] = []
        self._id_index: Dict[str, Student] = {}
    def add_student(self, student_data: dict) -> bool:
        id_number = student_data.get("id")
        first_name = student_data.get("first_name")
        last_name = student_data.get("last_name")
        grade_level = student_data.get("grade_level", 1)
        try:
            grade_int = int(grade_level)
        except (ValueError, TypeError):
            return False
        if not id_number or first_name is None or last_name is None:
            return False
        if len(self._students) >= self._capacity:
            return False
        new_student = Student(id_number, first_name, last_name, grade_int)
        if id_number in self._id_index:
            existing_id = self._id_index[id_number]
            print(f"Warning: Duplicate ID {id_number} found. Replacing.")
        self._students.append(new_student)
        self._id_index[id_number] = new_student
        return True
    def get_student_by_id(self, id_number: str) -> Student | None:
        if not isinstance(id_number, str):
            raise TypeError("ID must be a string.")
        return self._id_index.get(id_number)
    def get_all_students(self) -> List[Student]:
        result = [s for s in self._students]
        result.sort(key=lambda x: (x.grade_level, x.id))
        return result
    def remove_student_by_id(self, id_number: str) -> bool:
        if not isinstance(id_number, str):
            raise TypeError("ID must be a string.")
        existing = self._id_index.get(id_number)
        if not existing:
            return False
        index_in_list = list(self._students).index(existing)
        del self._students[index_in_list]
        del self._id_index[id_number]
        return True
    def __len__(self) -> int:
        return len(self._students)
if __name__ == '__main__':
    STORAGE_CAPACITY = 100
    system = StudentStorageSystem(capacity=STORAGE_CAPACITY)
    SAMPLE_DATA: List[dict] = [
        {"id": "S001", "first_name": "Alice", "last_name": "Smith", "grade_level": 9},
        {"id": "S002", "first_name": "Bob", "last_name": "Jones", "grade_level": 8},
        {"id": "S003", "first_name": "Charlie", "last_name": "Brown", "grade_level": 10},
    ]
    for data in SAMPLE_DATA:
        system.add_student(data)
    print(f"Total students added: {len(system)}")
    alice = system.get_student_by_id("S001")
    if alice:
        print(f"Fetched Student (ID S001): Alice Smith, Grade {alice.grade_level}")
    all_students = system.get_all_students()
    for s in all_students:
        print(f"Student ID: {s.id}, Name: {s.first_name} {s.last_name}, Grade: {s.grade_level}")
    system.remove_student_by_id("S999")                                                                              
    print(f"Students after failed remove attempt: {len(system)}")