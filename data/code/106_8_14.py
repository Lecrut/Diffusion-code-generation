from datetime import datetime

def calculate_year_difference(date1: datetime, date2: datetime) -> int:
    delta = date2 - date1
    days = abs(delta.days)
    years = days // 365
    return years

if __name__ == '__main__':
    start_date = datetime(2010, 1, 1)
    end_date = datetime(2023, 6, 15)
    result = calculate_year_difference(start_date, end_date)
    print(result)