import datetime

def is_valid_date(date_str):
    try:
        datetime.datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def is_weekend(date_obj):
    weekday = date_obj.weekday()
    return weekday >= 5

if __name__ == '__main__':
    date_str = '2023-10-07'
    if is_valid_date(date_str):
        date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
        print(f"Is {date_str} a weekend? {is_weekend(date_obj)}")
    else:
        print(f"{date_str} is not a valid date.")