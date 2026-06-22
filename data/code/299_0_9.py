from datetime import datetime
WEEKEND_DAYS = {5, 6}

def is_weekend(date_str):
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    return date_obj.weekday() in WEEKEND_DAYS
if __name__ == '__main__':
    print(is_weekend('2023-10-07'))
    print(is_weekend('2023-10-08'))
    print(is_weekend('2023-10-09'))