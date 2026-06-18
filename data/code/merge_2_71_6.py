from typing import Tuple, Union
class TimeConverter:
    def __init__(self):
        self.unit_multipliers = {
            "s": 1,
            "m": 60,
            "h": 3600,
            "d": 86400,
            "w": 604800,
        }
    def parse_duration(self, duration_str: str) -> int:
        if not isinstance(duration_str, str):
            raise TypeError("Duration must be a string.")
        parts = duration_str.strip().split()
        total_seconds = 0
        for part in parts:
            value_part, unit_part = part.split(None, 1)
            try:
                value = int(value_part)
            except ValueError:
                raise ValueError(f"Invalid numeric value '{value_part}' in duration string.")
            if not self.unit_multipliers.get(unit_part):
                raise ValueError(f"Unsupported time unit '{unit_part}'. Supported units are s, m, h, d, w.")
            total_seconds += value * self.unit_multipliers[unit_part]
        return total_seconds
    def format_duration(self, seconds: int) -> str:
        if not isinstance(seconds, int):
            raise TypeError("Seconds must be an integer.")
        units = ["w", "d", "h", "m", "s"]
        multipliers = [604800, 86400, 3600, 60, 1]
        result_parts: list[str] = []
        remaining_seconds = seconds
        for unit in units:
            if remaining_seconds >= multipliers[units.index(unit)]:
                count = remaining_seconds // multipliers[units.index(unit)]
                if count > 0 or not result_parts:
                    result_parts.append(f"{count}{unit}")
                remaining_seconds %= multipliers[units.index(unit)]
        return "".join(result_parts).lstrip(" ")
if __name__ == '__main__':
    converter = TimeConverter()
    test_cases = [
        "1h30m45s",
        "2d",
        "90w",
        "100ms"                                                                        
    ]
    for duration_str in test_cases:
        try:
            seconds = converter.parse_duration(duration_str)
            formatted = converter.format_duration(seconds)
            print(f"{duration_str} -> {seconds}s")
            print(f"Formatted back: {formatted}")
        except Exception as e:
            print(f"Error processing '{duration_str}': {e}")
    test_seconds = [16570, 432000]
    for sec in test_seconds:
        try:
            formatted = converter.format_duration(sec)
            print(f"{sec}s -> {formatted}")
        except Exception as e:
            print(f"Error formatting {sec}: {e}")