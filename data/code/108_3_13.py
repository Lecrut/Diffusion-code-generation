import re

def validate_date(date_str):
    if not isinstance(date_str, str) or len(date_str) != 10:
        raise ValueError("Input must be a string of length 10")
    if not re.match(r'^\d{4}-\d{2}-\d{2}$', date_str):
        raise ValueError("Input must match the YYYY-MM-DD format")

def extract_day(date_str):
    validate_date(date_str)
    day = int(date_str.split('-')[2])
    return day

if __name__ == '__main__':
    sample_dates = ["2023-10-05", "2023-12-25", "2024-01-01"]
    for date in sample_dates:
        result = extract_day(date)
        print(f"Date: {date}, Day of the month: {result}")