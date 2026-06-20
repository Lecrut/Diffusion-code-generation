from datetime import date

DAY_NAMES = {
    0: 'Monday',
    1: 'Tuesday',
    2: 'Wednesday',
    3: 'Thursday',
    4: 'Friday',
    5: 'Saturday',
    6: 'Sunday'
}

def get_full_day_name(date_obj):
    if not isinstance(date_obj, date):
        raise ValueError("Input must be a datetime.date object")
    
    return DAY_NAMES[date_obj.weekday()]

if __name__ == '__main__':
    sample_date = date(2023, 10, 5)
    print(get_full_day_name(sample_date))