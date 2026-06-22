from datetime import datetime

def parse_date(date_str):
    return datetime.strptime(date_str, '%Y-%m-%d')

def calculate_range(dates):
    if not dates:
        raise ValueError("Date list cannot be empty")
    parsed_dates = [parse_date(date) for date in dates]
    start_date = min(parsed_dates)
    end_date = max(parsed_dates)
    return (start_date, end_date)

def days_difference(start_date, end_date):
    delta = end_date - start_date
    return abs(delta.days)

def find_date_range(dates):
    start_date, end_date = calculate_range(dates)
    return days_difference(start_date, end_date)

if __name__ == '__main__':
    sample_dates1 = ['2023-01-01', '2023-01-15', '2023-01-10']
    result1 = find_date_range(sample_dates1)
    print(f"Range of dates {sample_dates1}: {result1} days")

    sample_dates2 = ['2023-12-25', '2024-01-01']
    result2 = find_date_range(sample_dates2)
    print(f"Range of dates {sample_dates2}: {result2} days")