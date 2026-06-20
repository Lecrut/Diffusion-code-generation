import datetime

DAY_OF_WEEK_MAPPING = {
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
    weekday_index = date_obj.weekday()
    return DAY_OF_WEEK_MAPPING[weekday_index]

if __name__ == '__main__':
    sample_date = '2023-12-25'
    day_name = get_day_of_week(sample_date)
    print(day_name)