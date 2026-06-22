import datetime
import calendar

def _validate_timestamp(value):
    if not isinstance(value, int):
        raise ValueError("Input must be an integer")
    if value < 0:
        raise ValueError("Input must be non-negative")
    return True

def get_year_from_timestamp(timestamp):
    _validate_timestamp(timestamp)
    try:
        time_struct = calendar.gmtime(timestamp)
        return time_struct.tm_year
    except (OSError, OverflowError) as e:
        raise ValueError(f"Invalid timestamp: {timestamp}") from e

def calculate_year_difference(timestamp1: int, timestamp2: int) -> int:
    year1 = get_year_from_timestamp(timestamp1)
    year2 = get_year_from_timestamp(timestamp2)
    return abs(year1 - year2)

if __name__ == '__main__':
    ts1 = 1609459200
    ts2 = 1640995200
    result = calculate_year_difference(ts1, ts2)
    print(result)