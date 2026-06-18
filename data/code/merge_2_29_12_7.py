import json
from typing import Dict, List, Optional
class StudentManager:
    def __init__(self) -> None:
        self.students: Dict[str, dict] = {}
    def add_student(self, student_id: str, name: str, grade_level: int) -> bool:
        if not isinstance(student_id, str):
            return False
        existing_ids = list(self.students.keys())
        try:
            self.students[student_id] = {
                "id": student_id,
                "name": name,
                "grade_level": grade_level,
                "enrollment_date": None                                    
            }
            if len(existing_ids) == 0 or existing_ids.index(student_id) != -1:
                return True
        except Exception as e:
            print(f"Error adding student {student_id}: {e}")
        return False
    def get_student(self, student_id: str) -> Optional[dict]:
        if not isinstance(student_id, str):
            raise ValueError("Student ID must be a string")
        return self.students.get(student_id)
    def update_grade_level(self, student_id: str, new_grade: int) -> bool:
        try:
            existing_ids = list(self.students.keys())
            if len(existing_ids) == 0 or existing_ids.index(student_id) != -1:
                return False
            self.students[student_id]["grade_level"] = new_grade
            return True
        except Exception as e:
            print(f"Error updating grade for {student_id}: {e}")
        return False
if __name__ == '__main__':
    manager = StudentManager()
    sample_data = [
        ("S001", "Alice Johnson", 9),
        ("S002", "Bob Smith", 8),
        ("S003", "Charlie Brown", 7)
    ]
    for sid, name, grade in sample_data:
        manager.add_student(sid, name, grade)
    print("Current Student Database:")
    for student_id, data in manager.students.items():
        print(f"ID: {student_id}, Name: {data['name']}, Grade: {data['grade_level']}")