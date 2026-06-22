from datetime import datetime, timedelta
import calendar

DAYS_IN_WEEK = 7
MONTH_NAMES = {
    1: 'January', 2: 'February', 3: 'March', 4: 'April',
    5: 'May', 6: 'June', 7: 'July', 8: 'August',
    9: 'September', 10: 'October', 11: 'November', 12: 'December'
}

def compute_next_calendar_day(date_str: str) -> datetime:
    current_dt = datetime.strptime(date_str, '%Y-%m-%d')
    next_dt = current_dt + timedelta(days=1)
    return next_dt

if __name__ == '__main__':
    input_date = '2024-02-28'
    next_day = compute_next_calendar_day(input_date)
    print(next_day)