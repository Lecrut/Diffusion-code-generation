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
    delta = end_date - start_date
    return abs(delta.days)

if __name__ == '__main__':
    date1 = '2023-03-15'
    date2 = '2024-03-15'
    print(days_between_dates(date1, date2))