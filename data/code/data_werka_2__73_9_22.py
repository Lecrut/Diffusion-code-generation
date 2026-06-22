from datetime import date

def _parse_date_string(date_string: str) -> date:
    parts = date_string.split('-')
    if len(parts) != 3:
        raise ValueError(f"Expected YYYY-MM-DD format, got {date_string}")
    try:
        year = int(parts[0])
        month = int(parts[1])
        day = int(parts[2])
    except ValueError:
        raise ValueError(f"Non-integer components in {date_string}")
    return date(year, month, day)

def calculate_days_between(date1_str: str, date2_str: str) -> int:
    date1 = _parse_date_string(date1_str)
    date2 = _parse_date_string(date2_str)
    delta = date2 - date1
    return abs(delta.days)

if __name__ == '__main__':
    start_date = '2024-01-15'
    end_date = '2024-10-20'
    result = calculate_days_between(start_date, end_date)
    print(result)