from datetime import date, timedelta
from calendar import weekday
TARGET_WEEKDAY = weekday(1, 0, 0)
WEEKDAYS_PER_WEEK = 7

def compute_next_saturday(current_date: date) -> date:
    current_weekday = current_date.weekday()
    days_ahead = (TARGET_WEEKDAY - current_weekday) % WEEKDAYS_PER_WEEK
    return current_date + timedelta(days=days_ahead)
if __name__ == '__main__':
    reference_date = date(2023, 11, 1)
    calculated_saturday = compute_next_saturday(reference_date)
    print(calculated_saturday)