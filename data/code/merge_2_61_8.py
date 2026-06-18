class TimeConverter:
    def to_components(self, seconds):
        if not isinstance(seconds, (int, float)):
            raise TypeError("Input must be a number")
        hours = int(seconds // 3600)
        remaining_seconds_after_hours = seconds % 3600
        minutes = int(remaining_seconds_after_hours // 60)
        final_seconds = round(remaining_seconds_after_hours - (minutes * 60))
        return {
            'hours': hours,
            'minutes': minutes,
            'seconds': final_seconds
        }
    def to_formatted_string(self, seconds):
        components = self.to_components(seconds)
        h_str = f"{components['hours']:02d}" if isinstance(components['hours'], int) else str(int(components['hours']))
        m_str = f"{components['minutes']:02d}" if isinstance(components['minutes'], int) else str(int(components['minutes']))
        s_str = f"{int(components['seconds']):02d}"
        return f"{h_str}:{m_str}:{s_str}"
if __name__ == '__main__':
    converter = TimeConverter()
    test_seconds_int = 3665
    result_dict = converter.to_components(test_seconds_int)
    print(f"Integer Input: {test_seconds_int}")
    print("Components:", result_dict)
    print("Formatted String:", converter.to_formatted_string(test_seconds_int))
    test_float_input = 72.984365
    float_result = converter.to_components(test_float_input)
    formatted_float = converter.to_formatted_string(test_float_input)
    print(f"\nFloat Input: {test_float_input}")
    print("Components:", float_result)
    print("Formatted String:", formatted_float)