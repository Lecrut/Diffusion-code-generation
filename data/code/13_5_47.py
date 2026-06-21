from datetime import date

def is_leap_year(year: int) -> bool:
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def days_in_month(year: int, month: int) -> int:
    if month in {1, 3, 5, 7, 8, 10, 12}:
        return 31
    elif month in {4, 6, 9, 11}:
        return 30
    elif month == 2 and is_leap_year(year):
        return 29
    elif month == 2:
        return 28
    else:
        raise ValueError("Invalid month")

def days_between_dates(date1: str, date2: str) -> int:
    start_date = date.fromisoformat(date1)
    end_date = date.fromisoformat(date2)
    
    if start_date > end_date:
        start_date, end_date = end_date, start_date
    
    delta = (end_date - start_date).days
    return delta

if __name__ == '__main__':
    date1 = '2023-01-01'
    date2 = '2024-02-29'
    try:
        result = days_between_dates(date1, date2)
        print(result)
    except ValueError as e:
        print(e)