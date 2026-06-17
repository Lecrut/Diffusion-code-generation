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
            'seconds': int(secs),
            'total_seconds': seconds
        }
    def to_formatted_string(self, seconds):
        components = self.to_components(seconds)
        if isinstance(components['hours'], float):
            h_str = f"{int(components['hours'])}:00"
        else:
            h_str = str(int(components['hours']))
        m_str = f"{components['minutes']:02d}"
        s_str = f"{components['seconds']:02d}"
        return f"{h_str}:{m_str}:{s_str}"
if __name__ == '__main__':
    converter = TimeConverter()
    test_seconds_int = 3661
    result_dict = converter.to_components(test_seconds_int)
    print(f"Integer Input: {test_seconds_int}")
    print("Dict Output:", result_dict)
    print("String Output:", converter.to_formatted_string(test_seconds_int))
    test_float_input = 7259.8
    try:
        float_result = converter.to_components(float(test_float_input))
        print(f"Float Input: {float(test_float_input)}")
        print("Dict Output:", float_result)
        print("String Output:", converter.to_formatted_string(int(round(float(test_float_input)))) if isinstance(result_dict, dict) else "Skipped for consistency check logic above")
    except Exception as e:
        pass
    sample_cases = [0, 61, 3600, 86400]
    print("\n--- Sample Cases ---")
    for sec in sample_cases:
        d_out = converter.to_components(sec)
        s_out = converter.to_formatted_string(sec)
        print(f"Seconds ({sec}): {s_out} -> Components: hours={d_out['hours']}, mins={d_out['minutes']}, secs={d_out['seconds']}")