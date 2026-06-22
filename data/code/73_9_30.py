from datetime import datetime, timedelta

def parse_date_string(date_str: str) -> datetime:
    if len(date_str) != 10 or date_str[4] != '-' or date_str[7] != '-':
        raise ValueError("Date string must be in YYYY-MM-DD format")
    try:
        return datetime.strptime(date_str, '%Y-%m-%d')
    except ValueError:
        raise ValueError(f"Invalid date value in string: {date_str}")

def calculate_days_between(date1_str: str, date2_str: str) -> int:
    d1 = parse_date_string(date1_str)
    d2 = parse_date_string(date2_str)
    delta = d2 - d1
    return delta.days

if __name__ == '__main__':
    start = '2023-01-01'
    end = '2023-12-31'
    result = calculate_days_between(start, end)
    print(result)