import datetime
import calendar

def get_remaining_minutes_in_current_month():
    now = datetime.datetime.now()
    year = now.year
    month = now.month
    last_day = calendar.monthrange(year, month)[1]
    last_day_datetime = datetime.datetime(year, month, last_day, 23, 59, 59)
    remaining_seconds = (last_day_datetime - now).total_seconds()
    remaining_minutes = int(remaining_seconds / 60)
    return remaining_minutes

if __name__ == '__main__':
    result = get_remaining_minutes_in_current_month()
    print(result)