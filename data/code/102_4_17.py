from datetime import datetime
WEEKDAY_NAMES = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
WEEKEND_DAYS = {5, 6}

def check_weekday(date_string: str) -> str:
    try:
        date_obj = datetime.strptime(date_string, '%Y-%m-%d')
        weekday_index = date_obj.weekday()
        if weekday_index in WEEKEND_DAYS:
            return 'Weekend'
        else:
            return f'{WEEKDAY_NAMES[weekday_index]}'
    except ValueError:
        return 'Invalid Date Format'
if __name__ == '__main__':
    dates = ['2023-10-23', '2023-10-28', '2023-10-29', '2023-10-30', '2023-10-31', '2023-11-01']
    for date in dates:
        print(check_weekday(date))