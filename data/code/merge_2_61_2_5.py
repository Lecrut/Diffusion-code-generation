class TimeConverter:
    def convert_seconds_to_hms(self, seconds):
        if not isinstance(seconds, (int, float)) or seconds < 0:
            raise ValueError("Input must be a non-negative number.")
        hours = int(seconds // 3600)
        remaining_minutes = int((seconds % 3600) / 60)
        minutes = remaining_minutes
        return f"{hours}h {minutes}m"
if __name__ == '__main__':
    converter = TimeConverter()
    test_cases = [
        (12345, "Expected: 3h 29m"),
        (0, "Expected: 0h 0m"),
        (86400, "Expected: 24h 0m"),
        (7.5, "Expected: 0h 1m")
    ]
    for seconds, expected in test_cases:
        result = converter.convert_seconds_to_hms(seconds)
        print(f"Input: {seconds}s -> Output: {result} | Expected: {expected}")