import json
class RobustDataAppender:
    def __init__(self):
        self.data = []
    def append_entry(self, entry_type: str, value) -> bool:
        try:
            if not isinstance(entry_type, str):
                raise TypeError("Entry type must be a string.")
            valid_types = ["integer", "float", "string"]
            if entry_type.lower() not in valid_types:
                return False
            validated_value = None
            error_msg = ""
            try:
                if entry_type.lower() == "integer":
                    int_val = int(value)
                    validated_value = {"type": "integer", "value": int_val}
                elif entry_type.lower() == "float":
                    float_val = float(value)
                    validated_value = {"type": "float", "value": float_val}
                else:          
                    str_val = str(value) if value is not None else ""
                    validated_value = {"type": "string", "value": str_val}
            except (ValueError, TypeError):
                error_msg = f"Invalid conversion for {entry_type}: '{value}'."
            self.data.append(validated_value)
            return True
        except Exception as e:
            print(f"Unexpected error during append: {e}")
            return False
if __name__ == '__main__':
    appender = RobustDataAppender()
    test_cases = [
        ("integer", "42"),
        ("float", "3.14"),
        ("string", "Hello World"),
        ("invalid_type", "test"),
        ("integer", "not_a_number"),
        (None, 99),
    ]
    for entry_type, value in test_cases:
        result = appender.append_entry(entry_type, value)
        print(f"Appended {entry_type} '{value}' -> Success: {result}")