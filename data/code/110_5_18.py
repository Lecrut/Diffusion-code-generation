from datetime import datetime
from functools import cmp_to_key

DATE_FORMAT = '%d/%m/%Y'
MONTHS = {
    '01': 1, '02': 2, '03': 3, '04': 4, '05': 5, '06': 6,
    '07': 7, '08': 8, '09': 9, '10': 10, '11': 11, '12': 12
}

def parse_date_string(date_str):
    parts = date_str.split('/')
    if len(parts) != 3:
        raise ValueError(f"Expected 3 parts, got {len(parts)}")
    day_str, month_str, year_str = parts
    if month_str not in MONTHS:
        raise ValueError(f"Invalid month string: {month_str}")
    month = MONTHS[month_str]
    day = int(day_str)
    year = int(year_str)
    return datetime(year=year, month=month, day=day)

def compare_dates(date_a, date_b):
    dt_a = parse_date_string(date_a)
    dt_b = parse_date_string(date_b)
    if dt_a < dt_b:
        return -1
    elif dt_a > dt_b:
        return 1
    return 0

def sort_dates(date_strings):
    if not date_strings:
        return []
    sorted_dates = sorted(date_strings, key=cmp_to_key(compare_dates))
    return sorted_dates

if __name__ == '__main__':
    sample_dates = ['25/12/2023', '01/01/2024', '15/06/2023', '31/12/2022']
    result = sort_dates(sample_dates)
    print(result)