import calendar
import datetime

def compute_weekday(year: int, month: int, day: int) -> str:
    target_date = datetime.date(year, month, day)
    weekday_index = target_date.weekday()
    weekday_name = calendar.day_name[weekday_index]
    return weekday_name

if __name__ == '__main__':
    year_val = 2025
    month_val = 3
    day_val = 15
    computed_day = compute_weekday(year_val, month_val, day_val)
    print(computed_day)