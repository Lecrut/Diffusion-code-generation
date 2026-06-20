from datetime import datetime

def parse_date(date_str):
    try:
        return datetime.strptime(date_str, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Invalid date format. Please use 'YYYY-MM-DD'.")

def calculate_days_between_dates(date1, date2):
    if date1 is None or date2 is None:
        raise ValueError("Both dates must be provided.")
    
    dt1 = parse_date(date1)
    dt2 = parse_date(date2)
    
    delta = abs(dt2 - dt1)
    return delta.days

if __name__ == '__main__':
    date1 = '2023-01-01'
    date2 = '2023-01-15'
    days_difference = calculate_days_between_dates(date1, date2)
    print(f"Days between {date1} and {date2}: {days_difference}")

    date3 = '2024-05-01'
    date4 = '2024-05-01'
    days_difference2 = calculate_days_between_dates(date3, date4)
    print(f"Days between {date3} and {date4}: {days_difference2}")

    date5 = '2023-12-31'
    date6 = '2024-01-01'
    days_difference3 = calculate_days_between_dates(date5, date6)
    print(f"Days between {date5} and {date6}: {days_difference3}")