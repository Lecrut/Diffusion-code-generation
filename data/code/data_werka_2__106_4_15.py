from datetime import datetime

def calculate_year_difference(start_date: datetime, end_date: datetime) -> int:
    if not isinstance(start_date, datetime) or not isinstance(end_date, datetime):
        raise ValueError("Both inputs must be datetime objects")
    delta = end_date - start_date
    total_days = abs(delta.days)
    years = total_days // 365
    return years

if __name__ == '__main__':
    date_one = datetime(2010, 5, 15)
    date_two = datetime(2020, 8, 20)
    difference = calculate_year_difference(date_one, date_two)
    print(difference)