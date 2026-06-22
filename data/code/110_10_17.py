from datetime import datetime
import calendar

DATE_FORMAT = '%Y-%m-%d'
MIN_YEAR = 1900
MAX_YEAR = 2100

def _validate_date_string(date_str):
    if not isinstance(date_str, str):
        raise ValueError("Input must be a string")
    parts = date_str.split('-')
    if len(parts) != 3:
        raise ValueError("Date format must be YYYY-MM-DD")
    year, month, day = parts
    if len(year) != 4 or len(month) != 2 or len(day) != 2:
        raise ValueError("Date components must have correct lengths")
    try:
        y, m, d = int(year), int(month), int(day)
    except ValueError:
        raise ValueError("Date components must be numeric")
    if y < MIN_YEAR or y > MAX_YEAR:
        raise ValueError("Year out of reasonable range")
    if m < 1 or m > 12:
        raise ValueError("Month out of range")
    max_day = calendar.monthrange(y, m)[1]
    if d < 1 or d > max_day:
        raise ValueError("Day out of range for month/year")
    return datetime(y, m, d)

def sort_dates(date_strings):
    if not date_strings:
        return []
    validated_dates = [_validate_date_string(d) for d in date_strings]
    paired = list(zip(date_strings, validated_dates))
    sorted_pairs = sorted(paired, key=lambda x: x[1])
    return [p[0] for p in sorted_pairs]

if __name__ == '__main__':
    sample_dates = ['2023-10-01', '2021-05-15', '2022-01-01', '2023-01-01']
    result = sort_dates(sample_dates)
    print(result)