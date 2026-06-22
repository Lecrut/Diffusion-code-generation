import datetime

def get_day_of_week(date_string):
    if not isinstance(date_string, str):
        raise TypeError("Date must be a string")
    if len(date_string) != 10:
        raise ValueError("Date string must be in YYYY-MM-DD format")
    parts = date_string.split("-")
    if len(parts) != 3:
        raise ValueError("Date string must contain exactly two dashes")
    year, month, day = parts
    if not year.isdigit() or not month.isdigit() or not day.isdigit():
        raise ValueError("Date components must be numeric")
    year_int = int(year)
    month_int = int(month)
    day_int = int(day)
    if month_int < 1 or month_int > 12:
        raise ValueError("Month must be between 1 and 12")
    if day_int < 1 or day_int > 31:
        raise ValueError("Day must be between 1 and 31")
    try:
        parsed_date = datetime.date(year_int, month_int, day_int)
        return parsed_date.strftime("%A")
    except ValueError:
        raise ValueError("Invalid calendar date")

if __name__ == '__main__':
    target_date = "2023-10-05"
    day_name = get_day_of_week(target_date)
    print(day_name)