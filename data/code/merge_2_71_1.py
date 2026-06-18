import re
from dataclasses import dataclass
@dataclass
class DurationResult:
    total_seconds: int | None = None
    error_message: str | None = None
def parse_duration(duration_str: str) -> DurationResult:
    pattern = r'^(\d+(?:\.\d+)?)\s*(h|hours?|hr)?\.?\s*([\d.]+)\s*m(?:inut(es)?)?$|^(\d+)\s*h\s+(\d+)(m|min)$'
    match = re.match(pattern, duration_str.strip(), re.IGNORECASE)
    if not match:
        return DurationResult(error_message="Invalid format")
    try:
        hours_part = float(match.group(1)) if match.group(2) else 0.0
        minutes_part = float(match.group(3)) or int(match.group(4)) if (match.group(3) and not match.group(5)) else int(match.group(5))
        total_seconds = round(hours_part * 3600 + minutes_part * 60)
        return DurationResult(total_seconds=total_seconds, error_message=None)
    except ValueError:
        return DurationResult(error_message="Invalid numeric value")
if __name__ == '__main__':
    test_cases = ['1h30m', '45min', '2.5 hours 10 minutes']
    for case in test_cases:
        result = parse_duration(case)
        print(f"Input: {case} -> Output: {result}")