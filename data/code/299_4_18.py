import datetime

def is_valid_date(date_string):
    try:
        datetime.datetime.strptime(date_string, '%m/%d/%Y')
        return True
    except ValueError:
        return False

def check_weekend(date_string):
    if not is_valid_date(date_string):
        return None
    date_obj = datetime.datetime.strptime(date_string, '%m/%d/%Y')
    weekday = date_obj.weekday()
    return weekday >= 5

if __name__ == '__main__':
    dates_to_check = [
        '01/01/2024',
        '01/06/2024',
        '03/15/2024',
        '12/25/2023',
        '02/17/2024'
    ]
    for date in dates_to_check:
        print(f"{date}: {check_weekend(date)}")