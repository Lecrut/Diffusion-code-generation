from datetime import datetime, timedelta

WEEKDAY_MONDAY = 0
WEEKS_IN_DAYS = 7

def get_next_monday(reference_date=None):
    if reference_date is None:
        reference_date = datetime.today()
    
    if not isinstance(reference_date, datetime):
        raise ValueError("reference_date must be a datetime object")
    
    current_weekday = reference_date.weekday()
    days_offset = (WEEKDAY_MONDAY - current_weekday) % WEEKS_IN_DAYS
    
    if days_offset == 0:
        days_offset = WEEKS_IN_DAYS
        
    return reference_date + timedelta(days=days_offset)

if __name__ == '__main__':
    sample_date = datetime(2023, 10, 25)
    result = get_next_monday(sample_date)
    print(result.strftime('%Y-%m-%d'))