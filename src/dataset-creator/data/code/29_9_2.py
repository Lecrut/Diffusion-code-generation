import json
from datetime import datetime
from pathlib import Path
class StudentStorage:
    def __init__(self, file_path: str = "students.json"):
        self.file_path = Path(file_path)
        if not self.file_path.exists():
            self.data = []
        else:
            try:
                with open(self.file_path, 'r', encoding='utf-8') as f:
                    self.data = json.load(f)
            except (json.JSONDecodeError, IOError):
                self.data = []
    def sanitize_input(self, name: str) -> bool:
        if not isinstance(name, str):
            return False
        stripped_name = name.strip()
        if len(stripped_name) < 2 or len(stripped_name) > 100:
            return False
        allowed_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_' ")
        for char in stripped_name:
            if char not in allowed_chars:
                return False
        return True
    def log_operation(self, operation: str, details: dict):
        timestamp = datetime.now().isoformat()
        entry = {
            "timestamp": timestamp,
            "operation": operation,
            "details": details
        }
        try:
            with open("audit_log.json", 'a', encoding='utf-8') as f:
                json.dump(entry, f)
        except IOError:
            print(f"Failed to write audit log for {operation}")
    def store_student(self, name: str):
        if not self.sanitize_input(name):
            raise ValueError("Invalid student name format")
        existing_names = [s["name"] for s in self.data]
        if any(existing_name == name.lower() for existing_name in existing_names):
            duplicate_info = {"duplicate_of": name}
            self.log_operation("STORAGE_FAILURE", {**{"error_type": "DUPLICATE"}, **duplicate_info})
            raise ValueError(f"Student '{name}' already exists")
        student_record = {
            "id": len(self.data) + 1,
            "name": name.lower(),
            "timestamp": datetime.now().isoformat()
        }
        self.log_operation("STORAGE_SUCCESS", {"student_name": name})
        self.data.append(student_record)
        try:
            with open(self.file_path, 'w', encoding='utf-8') as f:
                json.dump(self.data, f, indent=2)
        except IOError:
            raise RuntimeError("Failed to persist student data")
if __name__ == '__main__':
    storage = StudentStorage()
    sample_names = [
        "Alice Johnson",
        "Bob Smith_ Jr.",
        "Charlie 123",
        "@invalid#user!",
        "",
        "Diana Prince"
    ]
    for name in sample_names:
        try:
            storage.store_student(name)
            print(f"Stored: {name}")
        except ValueError as e:
            print(f"Error storing '{name}': {e}")