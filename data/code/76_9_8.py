import datetime

def calculate_days_between_dates(start_date_str: str, end_date_str: str) -> int:
    start_date = datetime.datetime.strptime(start_date_str, '%Y-%m-%d').date()
    end_date = datetime.datetime.strptime(end_date_str, '%Y-%m-%d').date()
    return abs((end_date - start_date).days)

if __name__ == '__main__':
    date1 = '2023-01-01'
    date2 = '2024-01-01'
    difference = calculate_days_between_dates(date1, date2)
    print(f"Difference between {date1} and {date2}: {difference} days")