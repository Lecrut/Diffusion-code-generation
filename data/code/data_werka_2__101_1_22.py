import calendar
import datetime

def get_weekday_name(year, month, day):
    if not (1 <= month <= 12):
        raise ValueError("Month out of range")
    if not (1 <= day <= 31):
        raise ValueError("Day out of range")
    try:
        date_instance = datetime.date(year, month, day)
        weekday_index = date_instance.weekday()
        weekday_name = calendar.day_name[weekday_index]
        return weekday_name
    except ValueError as e:
        raise ValueError(f"Invalid date: {year}-{month}-{day}") from e

if __name__ == '__main__':
    target_year = 2024
    target_month = 2
    target_day = 29
    computed_weekday = get_weekday_name(target_year, target_month, target_day)
    print(computed_weekday)