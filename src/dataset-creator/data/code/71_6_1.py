from typing import Union
class TimeConverter:
    def __init__(self):
        self.unit_multipliers = {
            's': 1,
            'm': 60,
            'h': 3600,
            'd': 86400,
        }
    def parse_duration(self, duration_str: str) -> int:
        if not isinstance(duration_str, str):
            raise TypeError("Duration must be provided as a string.")
        parts = duration_str.strip().split()
        if len(parts) == 0:
            return 0
        total_seconds = 0
        for part in parts:
            try:
                value = int(part.split()[0])
            except ValueError:
                raise ValueError(f"Invalid number format found in duration string.")
            unit_char = part[-1] if part else ''
            if not isinstance(value, (int, float)):
                raise TypeError("Time values must be numeric integers or floats.")
            multiplier = self.unit_multipliers.get(unit_char)
            if multiplier is None:
                raise ValueError(f"Unsupported time unit '{unit_char}'. Supported units: {', '.join(self.unit_multipliers.keys())}")
            total_seconds += int(value * multiplier)
        return total_seconds
    def format_duration(self, seconds: Union[int, float]) -> str:
        if not isinstance(seconds, (int, float)):
            raise TypeError("Duration must be provided as an integer or float.")
        d = int(abs(seconds) // 86400) % 24
        h = int((abs(seconds) - d * 86400) // 3600)
        m = int(((abs(seconds) - (d * 86400 + h * 3600)) // 60))
        if seconds < 0:
            return f"-{self._format_positive(m, h, d)}"
        parts = []
        if m > 0 or h == 0 and d == 0:
            parts.append(f"{m}min")
        if h > 0:
            parts.append(f"{h}hr")
        if d > 0:
            parts.append(f"{d}day")
        return " ".join(parts)
if __name__ == '__main__':
    converter = TimeConverter()
    test_cases = [
        '1h30m45s',
        '2d5h10m',
        '-15m',
        '90min'
    ]
    for duration_str in test_cases:
        try:
            seconds = converter.parse_duration(duration_str)
            formatted = converter.format_duration(seconds)
            print(f"Input: {duration_str} -> Seconds: {seconds} -> Formatted: {formatted}")
        except Exception as e:
            print(f"Error processing '{duration_str}': {e}")
    sample_seconds = 3601.5
    try:
        formatted_output = converter.format_duration(sample_seconds)
        original_back_to_seconds = converter.parse_duration(formatted_output.replace('min', 'm').replace('hr', 'h'))
        print(f"Sample seconds ({sample_seconds}) -> Formatted: {formatted_output} -> Back to Seconds (approx): {original_back_to_seconds}")
    except Exception as e:
        print(f"Error processing sample value: {e}")