import re
class TimeConverter:
    def _validate_input(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Input must be an integer or float representing seconds.")
        if value < 0:
            raise ValueError("Seconds cannot be negative.")
    def to_formatted_time(self, total_seconds):
        self._validate_input(total_seconds)
        hours = int(total_seconds // 3600)
        remaining_seconds = (total_seconds % 3600)
        minutes = int(remaining_seconds // 60)
        seconds = round(remaining_seconds % 60, 2)
        if hours > 0:
            return f"{hours}h {minutes}m {seconds}s"
        elif minutes > 0:
            return f"{minutes}m {seconds}s"
        else:
            return f"{seconds}s"
if __name__ == '__main__':
    converter = TimeConverter()
    test_cases = [3661, 90.5, 7200]
    for sec in test_cases:
        try:
            result = converter.to_formatted_time(sec)
            print(f"{sec} seconds -> {result}")
        except (TypeError, ValueError) as e:
            print(f"Error processing {sec}: {e}")