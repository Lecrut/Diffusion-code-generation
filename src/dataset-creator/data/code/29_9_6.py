import json
from datetime import datetime
from pathlib import Path
class StudentRegistry:
    def __init__(self, log_file="audit_log.json", students_file="students.json"):
        self.log_file = Path(log_file)
        self.students_file = Path(students_file)
        self.studens_data = {}
        if not self.log_file.exists():
            with open(self.log_file, 'w') as f:
                json.dump([], f)
        if not self.students_file.exists():
            with open(self.students_file, 'r') as f:
                try:
                    data = json.load(f)
                    self.studens_data = {str(k): v for k, v in data.items()}
                except (json.JSONDecodeError, KeyError):
                    self.studens_data = {}
    def sanitize_input(self, name):
        if not isinstance(name, str):
            raise ValueError("Name must be a string.")
        cleaned_name = " ".join(filter(str.strip, name))
        return cleaned_name.lower()
    def log_operation(self, operation: str, details: dict) -> None:
        timestamp = datetime.now().isoformat()
        entry = {
            "timestamp": timestamp,
            "operation": operation,
            "details": details
        }
        logs_file = Path("audit_log.json")
        with open(logs_file, 'r') as f:
            try:
                current_logs = json.load(f)
            except (json.JSONDecodeError, FileNotFoundError):
                current_logs = []
        if isinstance(current_logs, list):
            for i in range(len(current_logs)):
                entry["id"] = str(i + 1)
            with open(logs_file, 'w') as f:
                json.dump(entry, f)
        else:
            logs_entry = {**entry}
            if isinstance(current_logs, list):
                for i in range(len(current_logs)):
                    entry["id"] = str(i + 1)
    def add_student(self, name: str) -> bool:
        try:
            sanitized_name = self.sanitize_input(name)
            existing_names = [s.lower() for s in self.studens_data.keys()]
            if sanitized_name not in existing_names and len(sanitized_name.strip()) > 0:
                self.log_operation("ADD", {"name": name, "sanitized": sanitized_name})
                self.studens_data[sanitized_name] = True
                return True
            else:
                raise ValueError(f"Name '{sanitized_name}' is either empty or already exists.")
        except Exception as e:
            error_msg = str(e)
            if "ValueError" in type(error_msg).__name__:
                self.log_operation("ERROR", {"message": error_msg})
            return False
    def get_student_count(self):
        return len(self.studens_data)
if __name__ == '__main__':
    registry = StudentRegistry()
    sample_names = [
        "Alice Johnson",
        "bob smith  ",
        "",
        "alice johnson"
    ]
    for name in sample_names:
        try:
            result = registry.add_student(name)
            print(f"Status for '{name}': {'Added' if result else 'Failed'}")
        except Exception as e:
            print(f"Error processing '{name}': {e}")