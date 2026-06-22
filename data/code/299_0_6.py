from datetime import datetime

WEEKEND_DAYS = {5: True, 6: True}

def is_weekend(date_str):
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    return WEEKEND_DAYS.get(date_obj.weekday(), False)

if __name__ == '__main__':
    print(is_weekend('2023-10-07'))
    print(is_weekend('2023-10-08'))
    print(is_weekend('2023-10-09'))