from datetime import datetime
from dateutil.relativedelta import relativedelta

def is_within_one_week(date1: datetime, date2: datetime) -> bool:
    delta = relativedelta(date1, date2)
    days_diff = abs(delta.days)
    if days_diff < 7:
        return True
    if days_diff == 7:
        hours_diff = abs(delta.hours)
        minutes_diff = abs(delta.minutes)
        seconds_diff = abs(delta.seconds)
        if hours_diff == 0 and minutes_diff == 0 and seconds_diff == 0:
            return True
    return False

if __name__ == '__main__':
    d1 = datetime(2023, 10, 10, 12, 0, 0)
    d2 = datetime(2023, 10, 15, 12, 0, 0)
    result = is_within_one_week(d1, d2)
    print(result)