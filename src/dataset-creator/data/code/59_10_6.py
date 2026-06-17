import datetime
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
def days_in_month(month, leap=False):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 29 if leap else 28
def get_day_of_week(year, month, day):
    try:
        date_obj = datetime.date(year, month, day)
        return "Monday" + str(date_obj.weekday())
    except ValueError as e:
        raise ValueError(f"Invalid date provided: {year}-{month}-{day}") from e
def calculate_day_of_week():
    sample_dates = [
        (2024, 3, 1),
        (2024, 6, 15),
        (2024, 2, 29),
        (2023, 7, 4)
    ]
    for y, m, d in sample_dates:
        try:
            result = get_day_of_week(y, m, d)
            print(f"{y}-{m}-{d}: {result}")
        except ValueError as ve:
            print(ve)
if __name__ == '__main__':
    calculate_day_of_week()