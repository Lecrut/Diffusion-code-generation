from datetime import date

def get_full_day_name(date_obj):
    if not isinstance(date_obj, date):
        raise ValueError("Input must be a date object")
    
    day_names = {
        0: 'Monday',
        1: 'Tuesday',
        2: 'Wednesday',
        3: 'Thursday',
        4: 'Friday',
        5: 'Saturday',
        6: 'Sunday'
    }
    return day_names[date_obj.weekday()]

if __name__ == '__main__':
    sample_date = date(2023, 10, 5)
    print(get_full_day_name(sample_date))