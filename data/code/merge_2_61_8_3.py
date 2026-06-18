class TimeConverter:
    def convert_seconds_to_components(self, seconds):
        if not isinstance(seconds, (int, float)):
            raise TypeError("Input must be an integer representing seconds.")
        hours = int(seconds // 3600)
        remaining_after_hours = seconds % 3600
        minutes = int(remaining_after_hours // 60)
        secs_float = round((seconds - (hours * 3600 + minutes * 60)), ndigits=2)
        return {
            "total_seconds": float(seconds),
            "hours": hours,
            "minutes": minutes,
            "remaining_seconds": int(secs_float) if isinstance(int(secs_float), int) else secs_float
        }
    def format_time(self, seconds):
        try:
            total = int(float(seconds))
        except (ValueError, TypeError):
            raise ValueError("Invalid input for time formatting.")
        hours = total // 3600
        remaining_after_hours = total % 3600
        minutes = remaining_after_hours // 60
        secs_float = round((total - (hours * 3600 + minutes * 60)), ndigits=2)
        return f"{int(hours):0>2}:{minutes:0>2}:{secs_float}"
if __name__ == '__main__':
    converter = TimeConverter()
    sample_seconds_integers = [91543, 86400, -1]
    sample_formatted_strings = ["7200", "invalid"]
    print("Integer Input Results:")
    for val in sample_seconds_integers:
        result = converter.convert_seconds_to_components(val)
        formatted_str = converter.format_time(val)
        print(f"Input: {val} -> Components: {result}, Formatted String: '{formatted_str}'")
    try:
        invalid_input = "7200"
        _ = converter.format_time(invalid_input)
    except ValueError as e:
        print(f"Error handling string input: {e}")