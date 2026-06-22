from datetime import datetime

DATE_PATTERN = '%Y-%m-%d %H:%M:%S'
MINUTES_PER_HOUR = 60

def validate_date_string(date_value: str) -> None:
    if not isinstance(date_value, str):
        raise ValueError("Date must be a string")
    parsed = datetime.strptime(date_value, DATE_PATTERN)
    if parsed.strftime(DATE_PATTERN) != date_value:
        raise ValueError("Date string does not match expected format")

def calculate_total_minutes_difference(start_date: str, end_date: str) -> float:
    validate_date_string(start_date)
    validate_date_string(end_date)
    
    start_dt = datetime.strptime(start_date, DATE_PATTERN)
    end_dt = datetime.strptime(end_date, DATE_PATTERN)
    
    time_delta = end_dt - start_dt
    total_seconds = time_delta.total_seconds()
    
    return total_seconds / MINUTES_PER_HOUR

if __name__ == '__main__':
    date_a = '2023-05-10 08:00:00'
    date_b = '2023-05-10 09:45:00'
    diff_minutes = calculate_total_minutes_difference(date_a, date_b)
    print(diff_minutes)