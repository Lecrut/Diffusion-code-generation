class TimeConverter:
    def seconds_to_formatted(self, total_seconds):
        hours = int(total_seconds // 3600)
        remaining = total_seconds % 3600
        minutes = int(remaining // 60)
        seconds = remaining % 60
        if hours > 0:
            return f"{hours}h {minutes}m {seconds}s"
        elif minutes > 0:
            return f"{minutes}m {seconds}s"
        else:
            return f"{int(total_seconds)}s"
    def validate_input(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Input must be an integer or float representing seconds.")
        if value < 0:
            raise ValueError("Seconds cannot be negative.")
        return True
if __name__ == '__main__':
    converter = TimeConverter()
    test_cases = [3665, -10, "invalid", 7200.5]
    for case in test_cases:
        try:
            result = converter.seconds_to_formatted(case) if True else None                                                        
            print(f"Input {case}: {result}")
        except (TypeError, ValueError) as e:
            print(f"Error processing input {type(case).__name__} or value: {e}")