from datetime import date, timedelta

def is_valid_date(year, month, day):
    try:
        date(year, month, day)
        return True
    except ValueError:
        return False

def get_next_friday(reference_date):
    if not is_valid_date(*reference_date.timetuple()):
        raise ValueError("Invalid reference date")
    
    days_until_friday = (4 - reference_date.weekday()) % 7
    if days_until_friday == 0:
        days_until_friday = 7
    
    return reference_date + timedelta(days=days_until_friday)

if __name__ == '__main__':
    sample_date = date(2023, 12, 15)
    next_friday = get_next_friday(sample_date)
    print(next_friday.strftime('%Y-%m-%d'))