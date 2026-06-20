import datetime

def validate_date_format(date_str: str) -> bool:
    try:
        datetime.datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def calculate_days_between_dates(start_date: str, end_date: str) -> int:
    if not (validate_date_format(start_date) and validate_date_format(end_date)):
        raise ValueError("Invalid date format. Please use ISO format (YYYY-MM-DD).")
    
    start = datetime.datetime.strptime(start_date, '%Y-%m-%d').date()
    end = datetime.datetime.strptime(end_date, '%Y-%m-%d').date()
    
    return abs((end - start).days)

if __name__ == '__main__':
    date_a = '2023-01-01'
    date_b = '2024-01-01'
    difference = calculate_days_between_dates(date_a, date_b)
    print(f"Days between {date_a} and {date_b}: {difference}")