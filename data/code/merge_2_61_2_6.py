class TimeConverter:
    def to_formatted_time(self, seconds: int) -> str:
        if not isinstance(seconds, int):
            raise TypeError("Input must be an integer")
        if seconds < 0:
            raise ValueError("Seconds cannot be negative")
        hours = seconds // 3600
        remaining_seconds = seconds % 3600
        minutes = remaining_seconds // 60
        return f"{hours}h {minutes}m"
if __name__ == '__main__':
    converter = TimeConverter()
    test_cases = [
        (1, "0h 0m"),
        (3599, "0h 59m"),
        (7261, "2h 1m"),
        (86400, "24h 0m")
    ]
    for input_val in [seconds for seconds, expected in test_cases]:
        result = converter.to_formatted_time(input_val)
        print(f"Input: {input_val} -> Output: {result}")