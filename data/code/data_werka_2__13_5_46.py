from datetime import date

def is_leap_year(year: int) -> bool:
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def days_in_month(year: int, month: int) -> int:
    month_days = {
        1: 31, 2: 28, 3: 31, 4: 30,
        5: 31, 6: 30, 7: 31, 8: 31,
        9: 30, 10: 31, 11: 30, 12: 31
    }
    if month == 2 and is_leap_year(year):
        return 29
    return month_days[month]

def days_between_dates(date1: str, date2: str) -> int:
    start_date = date.fromisoformat(date1)
    end_date = date.fromisoformat(date2)
    
    if start_date > end_date:
        start_date, end_date = end_date, start_date
    
    current_date = start_date
    total_days = 0
    
    while current_date < end_date:
        days_in_current_month = days_in_month(current_date.year, current_date.month)
        days_to_end_of_month = min(days_in_current_month - current_date.day + 1, (end_date - current_date).days)
        
        total_days += days_to_end_of_month
        current_date += timedelta(days=days_to_end_of_month)
    
    return total_days

if __name__ == '__main__':
    date1 = '2023-01-01'
    date2 = '2024-02-29'
    result = days_between_dates(date1, date2)
    print(result)