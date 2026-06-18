class TimeConverter:
    def convert_seconds_to_hms(self, seconds):
        if not isinstance(seconds, (int, float)):
            raise TypeError("Input must be an integer or float representing seconds.")
        hours = int(seconds // 3600)
        remaining_seconds_after_hours = seconds % 3600
        minutes = int(remaining_seconds_after_hours // 60)
        final_seconds = round(remaining_seconds_after_hours % 60, 2)
        return f"{hours}h {minutes}m {final_seconds}s"
    def validate_input(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError(f"Invalid input type: expected int or float, got {type(value).__name__}")
        if value < 0:
            raise ValueError("Seconds cannot be negative.")
        return True
if __name__ == '__main__':
    converter = TimeConverter()
    test_cases = [3661.5, -10, "invalid", None]
    for case in test_cases:
        try:
            result = converter.convert_seconds_to_hms(case)
            print(f"Input {case} -> Output: {result}")
        except (TypeError, ValueError) as e:
            print(f"Error processing input {case}: {e}")