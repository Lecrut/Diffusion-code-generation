import datetime

def determine_weekday(year, month, day):
    if year < 1 or month < 1 or month > 12 or day < 1:
        raise ValueError("Invalid date components")
    try:
        date_instance = datetime.date(year, month, day)
    except ValueError as e:
        raise ValueError(f"Invalid date: {e}")
    return date_instance.strftime("%A")

if __name__ == '__main__':
    target_year = 2024
    target_month = 2
    target_day = 29
    day_name = determine_weekday(target_year, target_month, target_day)
    print(day_name)