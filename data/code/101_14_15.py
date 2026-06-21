import calendar
import datetime

def get_march_15_weekday(year: int) -> str:
    if not isinstance(year, int) or year < 1:
        raise ValueError("Year must be a positive integer")
    target_date = datetime.date(year, 3, 15)
    return calendar.day_name[target_date.weekday()]

if __name__ == '__main__':
    sample_year = 2025
    computed_day = get_march_15_weekday(sample_year)
    print(computed_day)