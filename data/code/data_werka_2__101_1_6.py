import calendar
import datetime

def get_weekday_name(year, month, day):
    try:
        date_obj = datetime.date(year, month, day)
        return date_obj.strftime("%A")
    except ValueError as e:
        raise ValueError(f"Invalid date: {year}-{month}-{day}") from e

if __name__ == '__main__':
    sample_year = 2023
    sample_month = 10
    sample_day = 5
    weekday = get_weekday_name(sample_year, sample_month, sample_day)
    print(weekday)