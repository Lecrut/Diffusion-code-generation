import hashlib
import json
from datetime import datetime
from typing import Dict, List, Optional
class StudentRegistry:
    def __init__(self):
        self.students: set[str] = set()
        self.audit_log: List[Dict] = []
    def _sanitize_input(self, name: str) -> bool:
        if not isinstance(name, str):
            return False
        sanitized_name = name.strip().lower()
        forbidden_patterns = ["<", ">", "&", "\""]
        for char in forbidden_patterns:
            if char in sanitized_name:
                return False
        max_length = 50
        if len(sanitized_name) > max_length:
            sanitized_name = sanitized_name[:max_length]
        self.audit_log.append({
            "timestamp": datetime.now().isoformat(),
            "action": "SANITIZE",
            "input_type": type(name).__name__,
            "original_value": name,
            "result": sanitized_name
        })
        return True
    def _generate_hash(self, name: str) -> str:
        hash_input = f"{name}:{datetime.now().isoformat()}"
        return hashlib.sha256(hash_input.encode()).hexdigest()[:16]
    def add_student(self, name: str) -> bool:
        if not self._sanitize_input(name):
            self.audit_log.append({
                "timestamp": datetime.now().isoformat(),
                "action": "REJECT",
                "reason": "Invalid input format or characters"
            })
            return False
        unique_name = name.strip()
        if len(unique_name) == 0:
            self.audit_log.append({
                "timestamp": datetime.now().isoformat(),
                "action": "REJECT",
                "reason": "Empty string after sanitization"
            })
            return False
        existing_hash = None
        for stored in list(self.students):
            if unique_name.lower() == stored:
                self.audit_log.append({
                    "timestamp": datetime.now().isoformat(),
                    "action": "REJECT",
                    "reason": f"Duplicate name detected (original hash: {stored})"
                })
                return False
        new_hash = self._generate_hash(unique_name)
        self.students.add(new_hash)
        operation_log_entry = {
            "timestamp": datetime.now().isoformat(),
            "action": "ADD",
            "original_input": name,
            "normalized_value": unique_name.lower()
        }
        if new_hash in [s for s in self.students]:
            operation_log_entry["status"] = "SUCCESS"
        else:
            operation_log_entry["status"] = "FAILED"
        self.audit_log.append(operation_log_entry)
        return True
    def get_audit_trail(self) -> List[Dict]:
        return list(self.audit_log)
def log_operation(action_type: str, details: Dict):
    with open("audit_log.json", "a") as f:
        json.dump(details, f)
if __name__ == '__main__':
    registry = StudentRegistry()
    test_cases = [
        ("Alice Smith", True),
        ("<script>alert('xss')</script>", False),
        ("Bob Jones & Jane Doe", False),
        ("" ,False),
        ("charlie123", True)
    ]
    for input_name, expected_success in test_cases:
        try:
            result = registry.add_student(input_name)
            print(f"Input: {input_name!r} -> Success: {result}")
            if not result and "Duplicate name detected" in str(registry.audit_log[-1]):
                pass
        except Exception as e:
            log_operation("ERROR", {"error": str(e), "input": input_name})
    print("\nAudit Log Preview:")
    for entry in registry.get_audit_trail():
        if len(entry) > 0:
            print(f"Timestamp: {entry['timestamp']}, Action: {entry.get('action', 'UNKNOWN')}, Result: {'SUCCESS' if result else 'FAILED'}")