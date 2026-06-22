import datetime
WEEKEND_DAYS = {5, 6}

def is_weekend(date_string):
    try:
        date_obj = datetime.datetime.strptime(date_string, '%m/%d/%Y')
        return date_obj.weekday() in WEEKEND_DAYS
    except ValueError:
        return None
if __name__ == '__main__':
    dates_to_check = ['01/01/2024', '01/06/2024', '03/15/2024', '12/25/2023', '02/17/2024']
    for date in dates_to_check:
        print(f'{date}: {is_weekend(date)}')