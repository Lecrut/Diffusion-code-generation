import datetime

WEEKDAY_NAMES = {
    0: 'Monday',
    1: 'Tuesday',
    2: 'Wednesday',
    3: 'Thursday',
    4: 'Friday',
    5: 'Saturday',
    6: 'Sunday'
}

def get_day_of_week(date_string):
    date_obj = datetime.datetime.strptime(date_string, '%Y-%m-%d')
    day_index = date_obj.weekday()
    return WEEKDAY_NAMES[day_index]

if __name__ == '__main__':
    sample_date = '2023-10-05'
    print(get_day_of_week(sample_date))