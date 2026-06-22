from datetime import datetime
import calendar

MONTH_NAMES = {
    1: 'January', 2: 'February', 3: 'March', 4: 'April',
    5: 'May', 6: 'June', 7: 'July', 8: 'August',
    9: 'September', 10: 'October', 11: 'November', 12: 'December'
}

DAY_NAMES = {
    0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday',
    4: 'Friday', 5: 'Saturday', 6: 'Sunday'
}

def format_date_custom(date_obj):
    day_name = DAY_NAMES[date_obj.weekday()]
    month_name = MONTH_NAMES[date_obj.month]
    day = date_obj.day
    year = date_obj.year
    return f"{day_name}, {month_name} {day:02d}, {year}"

if __name__ == '__main__':
    sample_date = datetime(2023, 10, 25)
    formatted = format_date_custom(sample_date)
    print(formatted)