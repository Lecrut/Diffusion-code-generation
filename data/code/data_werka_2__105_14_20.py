import datetime

DAY_INDEX_MONDAY = 0
DAYS_IN_WEEK = 7

def get_next_monday(target_date=None):
    if target_date is None:
        target_date = datetime.date.today()
    
    current_weekday = target_date.weekday()
    days_until_monday = (DAY_INDEX_MONDAY - current_weekday) % DAYS_IN_WEEK
    
    if days_until_monday == 0:
        days_until_monday = DAYS_IN_WEEK
        
    next_monday = target_date + datetime.timedelta(days=days_until_monday)
    return next_monday

if __name__ == '__main__':
    sample_date = datetime.date(2023, 10, 15)
    result = get_next_monday(sample_date)
    print(result)