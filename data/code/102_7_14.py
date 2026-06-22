import calendar
from datetime import date

def validate_weekday_status(target_date):
    year_component = target_date.year
    month_component = target_date.month
    day_component = target_date.day
    numeric_day = calendar.weekday(year_component, month_component, day_component)
    return numeric_day < 5

if __name__ == '__main__':
    reference_date = date(2025, 12, 25)
    status_value = validate_weekday_status(reference_date)
    print(status_value)