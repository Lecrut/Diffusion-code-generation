import re
from typing import Tuple, Optional
class TimeConverter:
    def __init__(self):
        self.pattern = re.compile(r'(\d+(?:\.\d+)?)\s*(h|H|h|m|M|min|mi|minutes?|s|S|sec|seconds?)', re.IGNORECASE)
    def parse_to_seconds(self, duration_str: str) -> int:
        if not isinstance(duration_str, str):
            raise TypeError("Input must be a string.")
        matches = self.pattern.findall(duration_str.strip())
        total_seconds = 0
        for value_unit in matches:
            try:
                num = float(value[0])
                unit = value[1].lower() if len(value) > 1 else 's'
                multipliers = {'h': 3600, 'm': 60, 's': 1}
                total_seconds += int(num * multipliers.get(unit, 1))
            except ValueError:
                raise ValueError(f"Invalid number format found in duration string.")
        return total_seconds
    def convert_to_human(self, seconds: float) -> str:
        if not isinstance(seconds, (int, float)):
            raise TypeError("Input must be a numeric value representing seconds.")
        hours = int(seconds // 3600)
        remaining = seconds % 3600
        minutes = int(remaining // 60)
        secs = round(remaining % 60, 2)
        parts = []
        if hours > 0:
            parts.append(f"{hours}h")
        if minutes > 0 or (secs != 0 and not any(p for p in parts)):
            part_str = f"{minutes}m{secs}s" if secs != 0 else f"{minutes}m"
            parts.append(part_str)
        return " ".join(parts).strip()
if __name__ == '__main__':
    converter = TimeConverter()
    test_cases = [
        '1h30m45s',
        '2.5h',
        '90min',
        '60sec',
        '1d'                                                                                                                                                                                                                                                                                                                                
    ]
    print("Parsing results:")
    for test in test_cases:
        try:
            seconds = converter.parse_to_seconds(test)
            human_str = converter.convert_to_human(seconds)
            print(f"{test} -> {seconds}s -> {human_str}")
        except Exception as e:
            print(f"Error processing '{test}': {e}")
    reverse_tests = [3601, 7205.9]
    print("\nConversion results:")
    for sec in reverse_tests:
        try:
            human_str = converter.convert_to_human(sec)
            parsed_back = converter.parse_to_seconds(human_str)
            match_status = "Match" if abs(parsed_back - sec) < 0.1 else f"Difference ({abs(parsed_back - sec)})"
            print(f"{sec}s -> {human_str} (Round-trip: {match_status})")
        except Exception as e:
            print(f"Error processing value {sec}: {e}")