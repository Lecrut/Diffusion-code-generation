import json
from datetime import datetime
class BooleanValidator:
    def __init__(self):
        self.log_entries = []
    def log(self, message, level="INFO"):
        timestamp = datetime.now().isoformat()
        entry = {
            "timestamp": timestamp,
            "level": level,
            "message": message
        }
        self.log_entries.append(entry)
        print(f"[{level}] [{timestamp}] {message}")
    def validate_bool(self, value):
        if isinstance(value, bool):
            return True
        elif isinstance(value, int):
            if value == 0:
                return False
            else:
                self.log("Warning: Integer used as boolean", level="WARNING")
                return bool(value)
        elif isinstance(value, str):
            lower_val = value.lower()
            if lower_val in ("true", "1"):
                return True
            elif lower_val in ("false", "0"):
                self.log("Warning: String used as boolean", level="WARNING")
                return False
            else:
                raise ValueError(f"Invalid string representation for boolean: {value}")
        else:
            raise TypeError(f"Unsupported type for boolean validation: {type(value)}")
    def get_log_summary(self):
        warnings = sum(1 for e in self.log_entries if e["level"] == "WARNING")
        errors = sum(1 for e in self.log_entries if e["level"] != "INFO")
        return {"total_logs": len(self.log_entries), "warnings": warnings, "errors": 0}
if __name__ == '__main__':
    validator = BooleanValidator()
    test_cases = [True, False, 1, -1, 0, "", "true", "TRUE", "false", "FALSE"]
    for val in test_cases:
        try:
            result = validator.validate_bool(val)
            validator.log(f"Validated {val} -> {result}")
        except Exception as e:
            validator.log(str(e), level="ERROR")
    summary = validator.get_log_summary()
    print("\n--- Validation Summary ---")
    for key, value in summary.items():
        if isinstance(value, int):
            print(f"{key}: {value}")