from datetime import datetime
import re

INPUT_PATTERN = re.compile(r'^(\d{2})-(\d{2})-(\d{4}) (\d{2}):(\d{2}):(\d{2})$')

def parse_date_components(date_string: str) -> tuple:
    match = INPUT_PATTERN.match(date_string)
    if not match:
        raise ValueError(f"Invalid date format: {date_string}")
    day, month, year, hour, minute, second = match.groups()
    return int(year), int(month), int(day), int(hour), int(minute), int(second)

def convert_to_iso8601(date_string: str) -> str:
    year, month, day, hour, minute, second = parse_date_components(date_string)
    dt = datetime(year, month, day, hour, minute, second)
    return dt.isoformat()

if __name__ == '__main__':
    sample_date = '25-12-2023 14:30:00'
    result = convert_to_iso8601(sample_date)
    print(result)