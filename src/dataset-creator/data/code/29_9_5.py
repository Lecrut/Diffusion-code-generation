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
    def log_operation(self, operation, details=None):
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
            if not clean_name or len(clean_name) < 3:
                raise ValueError("Invalid student name")
            if clean_name in self.students:
                return False
            self.students[clean_name] = True
            details = f"Added new unique student: {clean_name}"
            self.log_operation("ADD_STUDENT", details=details)
            return True
        except Exception as e:
            error_msg = str(e)
            self.log_operation("ERROR", details=f"{error_msg} - Operation failed")
            raise
    def get_all_students(self):
        try:
            sorted_names = sorted(list(self.students.keys()))
            if not sorted_names:
                return []
            with open(self.data_file, 'w') as f:
                json.dump(sorted_names, f)
            details = "Retrieved and persisted all registered students"
            self.log_operation("GET_STUDENTS", details=details)
            return sorted_names
        except Exception as e:
            error_msg = str(e)
            self.log_operation("ERROR", details=f"{error_msg} - Retrieval failed")
            raise
if __name__ == '__main__':
    registry = StudentRegistry()
    sample_data = [
        "Alice Johnson",
        "Bob Smith",
        "",
        "Charlie Brown",
        "alice johnson"                                                                                                                                                                                                                                             
    ]
    successful_adds = []
    failed_adds = []
    try:
        for name in sample_data:
            result = registry.add_student(name)
            if result:
                successful_adds.append(f"Added {name}")
            else:
                failed_adds.append(f"Duplicate or invalid attempt with input: '{name}'")
    except Exception as e:
        print(f"Critical Error during batch processing: {e}")
    try:
        all_students = registry.get_all_students()
        print("Registered Students:", ", ".join(all_students))
        with open(registry.log_file, 'r') as f:
            logs = json.load(f)
        if not any(l['operation'] == "FINAL_STATUS" for l in logs):
            entry = {
                "timestamp": datetime.now().isoformat(),
                "operation": "FINAL_STATUS",
                "details": f"BATCH_COMPLETE. Successes: {len(successful_adds)}, Failures: {len(failed_adds)}"
            }
            logs.append(entry)
            with open(registry.log_file, 'w') as f:
                json.dump(logs, f, indent=2)
    except Exception as e:
        print("Failed to retrieve student list:", e)