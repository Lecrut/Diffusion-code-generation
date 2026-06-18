class TimeConverter:
    def to_components(self, seconds):
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        secs = int(seconds % 60)
        return {
            'hours': hours,
            'minutes': minutes,
            'seconds': secs
        }
    def to_formatted_string(self, seconds):
        components = self.to_components(seconds)
        h_str = f"{components['hours']:02d}" if components['hours'] > 0 else "0"
        m_str = f"{components['minutes']:02d}"
        s_str = f"{components['seconds']:02d}"
        return f"{h_str}:{m_str}:{s_str}"
if __name__ == '__main__':
    converter = TimeConverter()
    test_cases = [3665, 14987, -10]
    for sec in test_cases:
        print(f"Input seconds: {sec}")
        result_dict = converter.to_components(sec)
        print("Integer components:", result_dict)
        formatted_str = converter.to_formatted_string(sec)
        print("Formatted string:", formatted_str)