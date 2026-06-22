from datetime import datetime
from typing import NamedTuple

class DateComparisonResult(NamedTuple):
    earlier_date: str
    later_date: str
    is_earlier: bool

def parse_and_compare(iso_str_a: str, iso_str_b: str) -> DateComparisonResult:
    def validate_iso_format(s: str) -> datetime:
        try:
            return datetime.fromisoformat(s)
        except (ValueError, TypeError) as exc:
            raise ValueError(f"Invalid ISO 8601 format: {s}") from exc

    dt_a = validate_iso_format(iso_str_a)
    dt_b = validate_iso_format(iso_str_b)

    if dt_a <= dt_b:
        return DateComparisonResult(iso_str_a, iso_str_b, True)
    else:
        return DateComparisonResult(iso_str_b, iso_str_a, False)

if __name__ == '__main__':
    result = parse_and_compare("2024-05-10T15:30:00", "2024-05-10T14:30:00")
    print(result.earlier_date)
    print(result.later_date)
    print(result.is_earlier)