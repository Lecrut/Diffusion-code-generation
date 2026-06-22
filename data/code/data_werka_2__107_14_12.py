from datetime import datetime
import re

DATE_PATTERN = re.compile(r'^(\d{2})-(\d{2})-(\d{4}) (\d{2}):(\d{2}):(\d{2})$')

def validate_date_format(date_string: str) -> bool:
    if not isinstance(date_string, str):
        return False
    match = DATE_PATTERN.match(date_string)
    if not match:
        return False
    day, month, year, hour, minute, second = (int(x) for x in match.groups())
    if not (1 <= month <= 12):
        return False
    if not (1 <= day <= 31):
        return False
    if not (0 <= hour <= 23):
        return False
    if not (0 <= minute <= 59):
        return False
    if not (0 <= second <= 59):
        return False
    return True

def convert_to_iso8601(date_string: str) -> str:
    if not validate_date_format(date_string):
        raise ValueError(f"Unsupported date format: {date_string}")
    day, month, year, hour, minute, second = (int(x) for x in DATE_PATTERN.match(date_string).groups())
    dt = datetime(year=year, month=month, day=day, hour=hour, minute=minute, second=second)
    return dt.isoformat()

if __name__ == '__main__':
    sample_date = '25-12-2023 14:30:00'
    result = convert_to_iso8601(sample_date)
    print(result)