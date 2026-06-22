from datetime import date
import calendar

def format_date_custom(d):
    if not isinstance(d, date):
        raise ValueError("Input must be a date instance")
    if d.day < 1 or d.day > 31:
        raise ValueError("Invalid day")
    if d.month < 1 or d.month > 12:
        raise ValueError("Invalid month")
    day_name = calendar.day_name[d.weekday()]
    month_name = calendar.month_name[d.month]
    return f"{day_name}, {month_name} {d.day:02d}, {d.year}"

if __name__ == '__main__':
    sample_date = date(2023, 10, 25)
    print(format_date_custom(sample_date))