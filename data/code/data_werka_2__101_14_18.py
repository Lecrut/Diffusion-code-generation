import calendar
import datetime

def get_weekday_for_date(year: int, month: int, day: int) -> str:
    date_instance = datetime.date(year, month, day)
    weekday_number = date_instance.weekday()
    return calendar.day_name[weekday_number]

if __name__ == '__main__':
    sample_year = 2025
    sample_month = 3
    sample_day = 15
    computed_weekday = get_weekday_for_date(sample_year, sample_month, sample_day)
    print(computed_weekday)