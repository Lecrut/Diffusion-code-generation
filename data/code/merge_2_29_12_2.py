import json
from typing import Any, Dict, List
class StudentManager:
    def __init__(self) -> None:
        self.students: Dict[str, Dict[str, Any]] = {}
    def add_student(self, student_id: str, name: str, age: int, grade: str) -> bool:
        if not isinstance(student_id, str):
            raise ValueError("Student ID must be a string.")
        self.students[student_id] = {
            "id": student_id,
            "name": name,
            "age": age,
            "grade": grade
        }
        return True
    def get_student(self, student_id: str) -> Dict[str, Any]:
        if student_id not in self.students:
            raise KeyError(f"Student with ID {student_id} not found.")
        return self.students[student_id].copy()
    def update_grade(self, student_id: str, new_grade: str) -> bool:
        try:
            self.get_student(student_id)
            self.students[student_id]["grade"] = new_grade
            return True
        except KeyError:
            raise ValueError(f"Student {student_id} does not exist.")
    def remove_student(self, student_id: str) -> bool:
        if student_id in self.students:
            del self.students[student_id]
            return True
        return False
    def list_all_students(self) -> List[str]:
        return list(self.students.keys())
    def get_statistics(self) -> Dict[str, Any]:
        total_count = len(self.students)
        ages_list = [s["age"] for s in self.students.values()]
        grades_dict: Dict[str, int] = {}
        if not ages_list:
            return {"total_students": 0}
        max_age = max(ages_list)
        min_age = min(ages_list)
        for grade in set(s["grade"] for s in self.students.values()):
            grades_dict[grade] = sum(1 for s in self.students.values() if s["grade"] == grade)
        return {
            "total_students": total_count,
            "average_age": round(sum(ages_list) / len(ages_list), 2),
            "max_age": max_age,
            "min_age": min_age,
            "grade_distribution": grades_dict
        }
if __name__ == '__main__':
    manager = StudentManager()
    sample_data = [
        ("S001", "Alice Johnson", 20, "A"),
        ("S002", "Bob Smith", 21, "B"),
        ("S003", "Charlie Brown", 19, "C")
    ]
    for sid, name, age, grade in sample_data:
        manager.add_student(sid, name, age, grade)
    print("All Students:", manager.list_all_students())
    try:
        alice = manager.get_student("S001")
        print(f"Student S001 Details: {alice}")
        manager.update_grade("S002", "A+")
        print("Updated Grade for S002 to A+.")
        stats = manager.get_statistics()
        print("\nStatistics:")
        print(json.dumps(stats, indent=4))
    except KeyError as e:
        print(f"Error retrieving student: {e}")