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
                    str_val = str(value)
                    if not isinstance(str_val, str):
                        raise ValueError("String conversion failed.")
                    validated_value = {"type": "string", "value": str_val}
            except (ValueError, TypeError) as e:
                error_msg = f"Invalid value for {entry_type}: {str(e)}"
            if not validated_value and error_msg == "":
                return False
            self.data.append(validated_value)
            print(f"Successfully appended entry of type '{entry_type}'.")
            return True
        except Exception as e:
            print(f"Unexpected error occurred: {str(e)}")
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