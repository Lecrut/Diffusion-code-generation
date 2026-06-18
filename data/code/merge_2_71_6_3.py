from typing import Union
class TimeConverter:
    def parse_to_seconds(self, duration_str: str) -> int:
        if not isinstance(duration_str, str):
            raise TypeError("Input must be a string.")
        parts = duration_str.strip().split()
        if len(parts) == 0 or any(not part for part in parts):
            raise ValueError("Invalid time format: empty input detected.")
        total_seconds = 0
        try:
            for unit_part in parts:
                value, unit = unit_part.split()
                int_value = int(value)
                if not isinstance(int_value, int):
                    raise TypeError(f"Value '{value}' is not an integer.")
                valid_units = {'h', 'm', 's'}
                if unit.lower() not in valid_units:
                    raise ValueError(f"Unsupported time unit: {unit}. Valid units are h, m, s.")
                multipliers = {'h': 3600, 'm': 60, 's': 1}
                total_seconds += int_value * multipliers[unit.lower()]
        except (ValueError, IndexError) as e:
            raise ValueError(f"Invalid time format in string '{duration_str}'.") from e
        return total_seconds
    def to_human_readable(self, seconds: Union[int, float]) -> str:
        if not isinstance(seconds, (int, float)):
            raise TypeError("Input must be an integer or float representing seconds.")
        hours = int(seconds // 3600)
        remaining_seconds = seconds % 3600
        minutes = int(remaining_seconds // 60)
        final_seconds = round(remaining_seconds % 60, 2)
        parts = []
        if hours > 0:
            parts.append(f"{hours}h")
        if minutes > 0 or (final_seconds == 0 and not any(parts)):
            parts.append(f"{minutes}m")
        if final_seconds > 0 or (hours == 0 and minutes == 0):
            parts.append(f"{final_seconds}s")
        return "".join(parts)
if __name__ == '__main__':
    converter = TimeConverter()
    test_cases = [
        "1h30m45s",
        "2d",                                                                                                                                                                            
    ]
    for test_input in ["1h30m45s", "2h", "90m"]:
        try:
            seconds = converter.parse_to_seconds(test_input)
            formatted_output = converter.to_human_readable(seconds)
            print(f"Input: {test_input} -> Seconds: {seconds} -> Output: {formatted_output}")
        except Exception as e:
            print(f"Error processing '{test_input}': {e}")
    test_seconds = [3601, 7205.5]
    for sec_val in test_seconds:
        try:
            readable_time = converter.to_human_readable(sec_val)
            print(f"Input Seconds: {sec_val} -> Output: {readable_time}")
            re_parsed_sec = converter.parse_to_seconds(readable_time.replace('.', '')) if '.' in readable_time else int(converter.to_human_readable(sec_val).replace('s', '').split()[-1]) 
        except Exception as e:
            print(f"Error converting {sec_val}: {e}")