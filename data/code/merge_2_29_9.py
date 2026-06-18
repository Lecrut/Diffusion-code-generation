import json
from datetime import datetime
from pathlib import Path
class StudentRegistry:
    def __init__(self, log_file="audit_log.json"):
        self.log_file = log_file
        self.students = set()
        self._load_logs(log_file)
    def _load_logs(self, file_path):
        if not Path(file_path).exists():
            return
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                logs_data = json.load(f)
                for log in reversed(logs_data):
                    self.students.add(log['name'])
        except (json.JSONDecodeError, IOError):
            pass
    def _save_logs(self, file_path):
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(list(reversed([log for log in self._get_all_logs() if not (self.students and log['name'] in self.students)])), f)
        except IOError:
            pass
    def _add_log(self):
        return {
            "timestamp": datetime.now().isoformat(),
            "action": None,
            "details": ""
        }
    def add_student(self, name):
        try:
            if not isinstance(name, str) or len(name.strip()) == 0:
                raise ValueError("Invalid student name")
            sanitized_name = name.strip()
            existing_names = [n for n in self.students]
            if sanitized_name.lower() in [x.lower() for x in existing_names]:
                log_entry = {**self._add_log(), "action": "duplicate_attempt", "details": f"Attempted to add: '{sanitized_name}' (already exists)"}
                with open(self.log_file, 'r', encoding='utf-8') as f:
                    logs_data = json.load(f)
                    if not isinstance(logs_data, list):
                        logs_data = []
                    logs_data.append(log_entry)
                    with open(self.log_file, 'w', encoding='utf-8') as f_out:
                        json.dump(logs_data, f, indent=2)
                return False
            self.students.add(sanitized_name.lower())
            log_entry = {**self._add_log(), "action": "success", "details": f"Added student: '{sanitized_name}'"}
            with open(self.log_file, 'r', encoding='utf-8') as f:
                logs_data = json.load(f)
                if not isinstance(logs_data, list):
                    logs_data = []
                logs_data.append(log_entry)
                try:
                    with open(self.log_file, 'w', encoding='utf-8') as f_out:
                        json.dump(logs_data, f_out, indent=2)
                except IOError:
                    pass
            return True
        except Exception as e:
            log_entry = {**self._add_log(), "action": "error", "details": str(e)}
            with open(self.log_file, 'r', encoding='utf-8') as f:
                logs_data = json.load(f)
                if not isinstance(logs_data, list):
                    logs_data = []
                logs_data.append(log_entry)
                try:
                    with open(self.log_file, 'w', encoding='utf-8') as f_out:
                        json.dump(logs_data, f_out, indent=2)
                except IOError:
                    pass
            return False
    def get_student_count(self):
        return len(self.students)
if __name__ == '__main__':
    registry = StudentRegistry()
    sample_names = [
        "Alice Johnson",
        "bob smith",
        "",
        None,
        12345,
        "Charlie Davis"
    ]
    for name in sample_names:
        try:
            result = registry.add_student(name) if name is not None else False
            print(f"Status: {'Success' if result else 'Failed'}")
        except Exception as e:
            print(f"Error processing '{name}': {e}")
    count = registry.get_student_count()
    print(f"\nTotal unique students registered: {count}")