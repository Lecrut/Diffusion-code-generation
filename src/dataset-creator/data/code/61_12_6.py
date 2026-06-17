import time
class TimeConverter:
    def convert_to_hms(self, seconds):
        if not isinstance(seconds, (int, float)):
            raise TypeError("Input must be an integer or float representing seconds.")
        hours = int(seconds // 3600)
        remaining_seconds = seconds % 3600
        minutes = int(remaining_seconds // 60)
        final_seconds = round(remaining_seconds % 60, 2)
        return f"{hours:0>2}:{minutes:0>2}:{final_seconds:05.2f}"
    def validate_input(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError(f"Invalid input type {type(value).__name__}. Expected int or float.")
        return True
if __name__ == '__main__':
    converter = TimeConverter()
    test_cases = [3661.50, 7200, -90]
    for sec in test_cases:
        try:
            result = converter.convert_to_hms(sec)
            print(f"{sec} seconds -> {result}")
            if not converter.validate_input(sec):
                pass
        except (TypeError, ValueError) as e:
            print(f"Error processing {sec}: {e}")
    invalid_cases = ["abc", 3.14, None]
    for val in invalid_cases:
        try:
            result = converter.convert_to_hms(val)
            if not converter.validate_input(val):
                pass
        except Exception as e:
            print(f"Caught expected error for {val}: {e}")
    sample_output = "01:01:01.50", 7263, -90