class TimeConverter:
    def to_components(self, seconds):
        if not isinstance(seconds, (int, float)):
            raise TypeError("Input must be an integer representing seconds.")
        hours = int(seconds // 3600)
        remaining_seconds_after_hours = seconds % 3600
        minutes = int(remaining_seconds_after_hours // 60)
        secs = remaining_seconds_after_hours % 60
        return {
            'hours': hours,
            'minutes': minutes,
            'seconds': int(secs)
        }
    def to_formatted_string(self, seconds):
        components = self.to_components(seconds)
        h_str = f"{components['hours']:02d}" if isinstance(components['hours'], int) else str(int(components['hours']))
        m_str = f"{components['minutes']:02d}" if isinstance(components['minutes'], int) else str(int(components['minutes']))
        s_str = f"{int(components['seconds']):02d}"
        return f"{h_str}:{m_str}:{s_str}"
if __name__ == '__main__':
    converter = TimeConverter()
    sample_seconds_integers = [3661, 8945, 72]
    print("Integer Component Output:")
    for s in sample_seconds_integers:
        result = converter.to_components(s)
        print(f"Input ({s}) -> {result}")
    print("\nFormatted String Output:")
    formatted_results = []
    for s in sample_seconds_integers:
        string_result = converter.to_formatted_string(s)
        formatted_results.append(string_result)
    print(" | ".join(formatted_results))