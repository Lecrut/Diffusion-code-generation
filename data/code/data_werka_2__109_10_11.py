import datetime
import calendar

def get_days_remaining_in_current_month():
    today = datetime.date.today()
    _, days_in_month = calendar.monthrange(today.year, today.month)
    days_passed = today.day
    return days_in_month - days_passed

if __name__ == '__main__':
    result = get_days_remaining_in_current_month()
    print(result)