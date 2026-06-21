import datetime

def calculate_year_difference(start_date: datetime.datetime, end_date: datetime.datetime) -> int:
    if not isinstance(start_date, datetime.datetime) or not isinstance(end_date, datetime.datetime):
        raise ValueError("Both arguments must be datetime objects")
    
    if start_date > end_date:
        start_date, end_date = end_date, start_date
    
    years = end_date.year - start_date.year
    
    if (end_date.month, end_date.day) < (start_date.month, start_date.day):
        years -= 1
    
    return years

if __name__ == '__main__':
    date1 = datetime.datetime(2020, 5, 15, 10, 30, 0)
    date2 = datetime.datetime(2023, 5, 14, 10, 30, 0)
    result = calculate_year_difference(date1, date2)
    print(result)