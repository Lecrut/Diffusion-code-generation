import json
from datetime import datetime
from pathlib import Path
import re
class StudentRegistry:
    def __init__(self, log_file="student_audit.log", data_file="students.json"):
        self.data_file = Path(data_file)
        self.log_file = Path(log_file)
        self.students = {}
        if self.data_file.exists():
            try:
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    self.students = json.load(f)
            except (json.JSONDecodeError, IOError):
                self.students = {}
    def sanitize_name(self, name):
        if not isinstance(name, str):
            return None
        pattern = r'^[a-zA-Z\s\'\-]+$'
        if re.match(pattern, name.strip()):
            return name.strip()
        return None
    def log_operation(self, operation, details=""):
        timestamp = datetime.now().isoformat()
        entry = {
            "timestamp": timestamp,
            "operation": operation,
            "details": details if details else ""
        }
        with open(self.log_file, 'a', encoding='utf-8') as f:
            f.write(json.dumps(entry) + "\n")
    def add_student(self, name):
        sanitized = self.sanitize_name(name)
        if not sanitized:
            self.log_operation("ADD_FAILED", "Invalid or empty name provided")
            return False
        if sanitized in self.students:
            self.log_operation("ADD_DUPLICATE", f"Name '{sanitized}' already exists")
            return False
        try:
            student_id = len(self.students) + 1
            self.students[sanitized] = {
                "id": student_id,
                "status": "active"
            }
            self.log_operation("ADD_SUCCESS", f"Added '{sanitized}' with ID {student_id}")
        except Exception as e:
            self.log_operation("ADD_ERROR", str(e))
            return False
    def get_all_students(self):
        try:
            data = json.dumps({k: v for k, v in sorted(self.students.items())})
            with open(self.data_file, 'w', encoding='utf-8') as f:
                f.write(data)
            self.log_operation("DATA_SAVED", "Student list persisted")
        except Exception as e:
            self.log_operation("SAVE_ERROR", str(e))
    def remove_student(self, name):
        sanitized = self.sanitize_name(name)
        if not sanitized or sanitized not in self.students:
            self.log_operation("REMOVE_FAILED", f"Name '{sanitized}' not found")
            return False
        try:
            del self.students[sanitized]
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump({k: v for k, v in sorted(self.students.items())}, f)
            self.log_operation("REMOVE_SUCCESS", f"Removed '{sanitized}'")
        except Exception as e:
            self.log_operation("REMOVE_ERROR", str(e))
if __name__ == '__main__':
    registry = StudentRegistry()
    sample_names = [
        "Alice Johnson",
        "Bob Smith",
        "",
        12345,
        "Charlie O'Brien-III"
    ]
    for name in sample_names:
        result = registry.add_student(name)
        print(f"Attempted to add '{name}': {'Success' if result else 'Failed'}")
    registry.get_all_students()