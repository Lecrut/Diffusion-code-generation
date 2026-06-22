from datetime import datetime

def is_weekend(date_str):
    try:
        date_obj = datetime.strptime(date_str, '%Y-%m-%d').date()
        weekday = date_obj.weekday()
        return weekday >= 5
    except ValueError:
        return False

def is_holiday(date_str):
    holidays = ['2023-10-12']
    return date_str in holidays
if __name__ == '__main__':
    sample_date = '2023-10-12'
    if is_weekend(sample_date):
        print('Weekend')
    elif is_holiday(sample_date):
        print('Holiday')
    else:
        print('Neither weekend nor holiday')