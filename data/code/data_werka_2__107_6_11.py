from datetime import date
import calendar

DAY_INDEX_TO_NAME = {
    0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday',
    4: 'Friday', 5: 'Saturday', 6: 'Sunday'
}

MONTH_INDEX_TO_NAME = {
    1: 'January', 2: 'February', 3: 'March', 4: 'April',
    5: 'May', 6: 'June', 7: 'July', 8: 'August',
    9: 'September', 10: 'October', 11: 'November', 12: 'December'
}

def format_date_custom(d):
    if not isinstance(d, date):
        raise ValueError("Input must be a date instance")
    
    day_name = DAY_INDEX_TO_NAME[d.weekday()]
    month_name = MONTH_INDEX_TO_NAME[d.month]
    
    return f"{day_name}, {month_name} {d.day:02d}, {d.year}"

if __name__ == '__main__':
    sample_date = date(2023, 10, 25)
    print(format_date_custom(sample_date))