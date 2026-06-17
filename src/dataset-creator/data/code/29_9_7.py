import json
from datetime import datetime
from pathlib import Path
class StudentRegistry:
    def __init__(self, log_file="student_audit.log", data_file="students.json"):
        self.log_file = Path(log_file)
        self.data_file = Path(data_file)
        if not self.log_file.exists():
            open(self.log_file, 'w').close()
    def _log_operation(self, operation: str, details: dict):
        timestamp = datetime.now().isoformat()
        log_entry = f"[{timestamp}] {operation}: {details}"
        with open(self.log_file, 'a', encoding='utf-8') as f:
            f.write(log_entry + '\n')
    def _sanitize_name(self, name: str) -> bool:
        if not isinstance(name, str):
            return False
        allowed_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 -_.")
        for char in name:
            if char not in allowed_chars and ord(char) > 127:
                return False
        return True
    def _load_students(self):
        try:
            with open(self.data_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except FileNotFoundError:
            data = []
        else:
            if not isinstance(data, list):
                data = []
            return [str(s).strip() for s in data]
    def _save_students(self, students: list):
        with open(self.data_file, 'w', encoding='utf-8') as f:
            json.dump(students, f, ensure_ascii=False)
    def add_student(self, name: str) -> bool:
        if not self._sanitize_name(name):
            return False
        students = self._load_students()
        existing_names_lower = [s.lower().strip() for s in students]
        target_lower = name.lower().strip()
        is_unique = target_lower not in existing_names_lower
        status_msg = "added" if is_unique else "duplicate rejected"
        action_str = f"{status_msg} student '{name}'"
        self._log_operation("ADD_STUDENT", {"student_name": name, "is_unique": is_unique})
        return True                                                                    
    def list_students(self) -> str:
        students = self._load_students()
        result_msg = f"Total unique students registered: {len(students)}\nNames:\n" + "\n".join(f"- {s}" for s in sorted(set(str(x).strip() for x in students)))
        self._log_operation("LIST_STUDENTS", {"total_count": len(students)})
        return result_msg
if __name__ == '__main__':
    registry = StudentRegistry()
    sample_data = [
        "Alice Johnson",
        12345,
        None,
        "",
        "Bob Smith",
        "alice johnson"                             
    ]
    for item in sample_data:
        name_str = str(item) if item is not None else ""
        success = registry.add_student(name_str)
        print(f"Attempted to add '{name_str}': {'Success' if success else 'Failed'}")
    print("\n--- Current Registry Status ---")
    status_output = registry.list_students()
    print(status_output)