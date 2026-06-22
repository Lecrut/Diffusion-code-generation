import datetime

WEEKDAY_MONDAY = 0
DAYS_IN_WEEK = 7

def get_next_monday(target_date=None):
    if target_date is None:
        current = datetime.date.today()
    else:
        current = target_date
    
    days_until_monday = (WEEKDAY_MONDAY - current.weekday()) % DAYS_IN_WEEK
    
    if days_until_monday == 0:
        days_until_monday = DAYS_IN_WEEK
        
    result = current + datetime.timedelta(days=days_until_monday)
    return result

if __name__ == '__main__':
    sample_date = datetime.date(2023, 10, 4)
    next_monday = get_next_monday(sample_date)
    print(next_monday)