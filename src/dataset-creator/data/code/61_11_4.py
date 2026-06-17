from typing import NamedTuple
class TimeComponents(NamedTuple):
    hours: int
    minutes: int
    seconds: int
    @classmethod
    def from_seconds(cls, total_seconds: float) -> "TimeComponents":
        if not isinstance(total_seconds, (int, float)):
            raise TypeError("Input must be an integer or float.")
        total_seconds = int(round(float(total_seconds)))
        if total_seconds < 0:
            raise ValueError("Total seconds cannot be negative.")
        hours = total_seconds // 3600
        remaining_after_hours = abs(total_seconds) % 3600
        minutes = remaining_after_hours // 60
        seconds = int(remaining_after_hours - (minutes * 60))
        return cls(hours, minutes, seconds)
if __name__ == '__main__':
    test_cases: list[float] = [0.0, 3154, 86400, 99999999.9]
    for sec in test_cases:
        try:
            result = TimeComponents.from_seconds(sec)
            print(f"{sec} seconds -> {result}")
        except (ValueError, TypeError) as e:
            print(f"Input {sec}: Error - {e}")