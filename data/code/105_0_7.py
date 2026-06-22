from datetime import datetime, timedelta

WEEKDAY_MONDAY = 0
DAYS_IN_WEEK = 7
OFFSET_TO_NEXT = 7

def find_next_monday():
    today = datetime.today()
    current_weekday = today.weekday()
    days_to_add = (WEEKDAY_MONDAY - current_weekday) % DAYS_IN_WEEK
    if days_to_add == 0:
        days_to_add = OFFSET_TO_NEXT
    next_monday = today + timedelta(days=days_to_add)
    return next_monday

if __name__ == '__main__':
    result = find_next_monday()
    print(result.strftime('%Y-%m-%d'))