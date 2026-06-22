import calendar

WEEKDAY_START = 0
WEEKDAY_END = 7

def get_weekday_name(year, month, day):
    if not isinstance(year, int) or not isinstance(month, int) or not isinstance(day, int):
        raise ValueError("Inputs must be integers")
    try:
        date_value = calendar.date(year, month, day)
    except ValueError:
        raise ValueError(f"Invalid date: {year}-{month}-{day}")
    index = date_value.weekday()
    days_list = list(calendar.day_name)
    return days_list[index]

if __name__ == '__main__':
    year_val = 2024
    month_val = 2
    day_val = 29
    weekday_result = get_weekday_name(year_val, month_val, day_val)
    print(weekday_result)