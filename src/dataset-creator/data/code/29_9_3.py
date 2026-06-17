import json
from datetime import datetime
from pathlib import Path
class StudentRegistry:
    def __init__(self, log_file="audit_log.json", data_file="students.db"):
        self.log_file = Path(log_file)
        self.data_file = Path(data_file)
        self.students = {}
        if not self.log_file.exists():
            with open(self.log_file, 'w') as f:
                json.dump([], f)
    def sanitize_name(self, name):
        return ''.join(c for c in str(name).strip() if c.isalnum()) or "Unknown"
    def log_operation(self, operation, details=""):
        entry = {
            "timestamp": datetime.now().isoformat(),
            "operation": operation,
            "details": details
        }
        with open(self.log_file, 'r') as f:
            logs = json.load(f)
        logs.append(entry)
        with open(self.log_file, 'w') as f:
            json.dump(logs, f, indent=2)
    def add_student(self, name):
        try:
            clean_name = self.sanitize_name(name)
            if not clean_name or len(clean_name) < 1:
                raise ValueError("Invalid student name")
            if clean_name in self.students:
                return False
            self.students[clean_name] = True
            self.log_operation("ADD", f"Student added: {clean_name}")
            return True
        except Exception as e:
            self.log_operation("ERROR", str(e))
            raise
    def get_all_students(self):
        try:
            with open(self.data_file, 'r') as f:
                data = json.load(f)
            if isinstance(data, dict):
                return list(data.keys())
            elif isinstance(data, list):
                return [item.get('name', item) for item in data]
        except Exception as e:
            self.log_operation("ERROR", "Failed to read student database")
            raise
    def save_data(self):
        try:
            with open(self.data_file, 'w') as f:
                json.dump({k: v for k, v in self.students.items()}, f)
            return True
        except Exception as e:
            self.log_operation("ERROR", "Failed to save student database")
            raise
if __name__ == '__main__':
    registry = StudentRegistry()
    sample_names = ["Alice Johnson", "", "Bob Smith", None, 12345]
    for name in sample_names:
        try:
            result = registry.add_student(name)
            print(f"Name '{name}' -> {'Added' if result else 'Duplicate or Invalid'}")
        except ValueError as ve:
            print(f"Error processing '{name}': {ve}")