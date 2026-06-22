from datetime import datetime

def is_weekend(date_str):
    try:
        date_obj = datetime.strptime(date_str, '%Y-%m-%d').date()
        weekday = date_obj.weekday()
        return weekday >= 5
    except ValueError:
        return False

def is_holiday(date_str):
    holidays = ['2023-01-01', '2023-07-04', '2023-12-25']
    return date_str in holidays

def is_special_date(date_str):
    return is_weekend(date_str) or is_holiday(date_str)
if __name__ == '__main__':
    sample_date = '2023-10-12'
    result = is_special_date(sample_date)
    print(result)