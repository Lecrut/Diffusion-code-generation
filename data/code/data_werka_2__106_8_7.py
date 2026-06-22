from datetime import datetime

def calculate_year_difference(date1: datetime, date2: datetime) -> int:
    delta = date2 - date1
    days = delta.days
    years = abs(days) // 365
    if (days < 0) != (date2 < date1):
        years = -years
    return years

if __name__ == '__main__':
    start_date = datetime(2020, 1, 1)
    end_date = datetime(2023, 6, 15)
    result = calculate_year_difference(start_date, end_date)
    print(result)