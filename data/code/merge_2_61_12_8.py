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
            raise TypeError(f"Invalid input type {type(value).__name__}. Expected int or float.")
        if value < 0:
            raise ValueError("Seconds cannot be negative.")
        return True
if __name__ == '__main__':
    converter = TimeConverter()
    test_cases = [3661, -5, "invalid", 7265.9]
    for case in test_cases:
        try:
            result = converter.convert_to_hms(case)
            print(f"Input {case} -> Output: {result}")
        except (TypeError, ValueError) as e:
            print(f"Error processing input {case}: {e}")