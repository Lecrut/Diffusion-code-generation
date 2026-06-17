class TimeConverter:
    def convert_to_hms(self, seconds):
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        secs = int(seconds % 60)
        return f"{hours}:{minutes:02d}:{secs:02d}"
    def validate_input(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Input must be an integer or float representing seconds.")
        if value < 0:
            raise ValueError("Seconds cannot be negative.")
        return True
if __name__ == '__main__':
    converter = TimeConverter()
    test_cases = [3661, -5, "invalid", None]
    for case in test_cases:
        try:
            result = converter.convert_to_hms(case) if isinstance(case, (int, float)) else None
            print(f"Input {case}: Validated OK -> Output: {result}")
        except Exception as e:
            print(f"Input {case}: Error - {e}")
    valid_input = 7265.5
    is_valid = converter.validate_input(valid_input)
    if is_valid:
        formatted_time = converter.convert_to_hms(int(valid_input))
        print(f"\nValidated Input {valid_input} converted to: {formatted_time}")