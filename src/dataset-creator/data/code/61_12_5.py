class TimeConverter:
    def validate_input(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Input must be an integer or float representing seconds.")
        if value < 0:
            raise ValueError("Seconds cannot be negative.")
        return True
    def to_hms(self, seconds):
        self.validate_input(seconds)
        hours = int(seconds // 3600)
        remaining_seconds = (seconds % 3600)
        minutes = int(remaining_seconds // 60)
        final_seconds = round(remaining_seconds % 60)
        return f"{hours:02d}:{minutes:02d}:{final_seconds:02d}"
if __name__ == '__main__':
    converter = TimeConverter()
    test_cases = [3700, -5, "invalid", 1.5]
    for case in test_cases:
        try:
            result = converter.to_hms(case)
            print(f"Input {case} -> Output: {result}")
        except (TypeError, ValueError) as e:
            print(f"Error processing input {case}: {e}")