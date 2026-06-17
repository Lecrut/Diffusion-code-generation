from dataclasses import dataclass
import re
@dataclass(frozen=True)
class Duration:
    years: int = 0
    months: int = 0
    days: int = 0
    hours: int = 0
    minutes: int = 0
    seconds: int = 0
    def __add__(self, other: "Duration") -> "Duration":
        return Duration(
            years=self.years + other.years,
            months=self.months + other.months,
            days=self.days + other.days,
            hours=self.hours + other.hours,
            minutes=self.minutes + other.minutes,
            seconds=self.seconds + other.seconds,
        )
    def __radd__(self, other: int) -> "Duration":
        return self.__add__(other if isinstance(other, Duration) else Duration(seconds=other))
ISO_PATTERN = re.compile(
    r"^P(?:(\d+)Y)?(?:(\d+)M)?(?:(\d+)D)?(?:T(?:(\d+)H)?(?:(\d+)M)?(?:(\d+(?:[.]\d+)?)S)?)?$"
)
def parse_iso_duration(duration_str: str) -> Duration:
    match = ISO_PATTERN.match(duration_str.strip())
    if not match:
        raise ValueError(f"Invalid ISO 8601 duration string: {duration_str}")
    years, months, days, hours, minutes, seconds = (int(match.group(i)) for i in range(1, 7) if match.group(i))
    return Duration(years=years or 0, months=months or 0, days=days or 0, hours=hours or 0, minutes=minutes or 0, seconds=int(seconds) if seconds else 0)
if __name__ == '__main__':
    test_cases = [
        "P1D",
        "PT2H",
        "P3Y6M4DT12H30M5S",
        "PT1.5H",
        "-P1D"
    ]
    for case in test_cases:
        try:
            result = parse_iso_duration(case)
            print(f"Parsed '{case}': {result}")
        except ValueError as e:
            print(f"Error parsing '{case}': {e}")