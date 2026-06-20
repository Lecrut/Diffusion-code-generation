import datetime

def get_day_of_week(date_string):
    days_mapping = {
        0: 'Monday',
        1: 'Tuesday',
        2: 'Wednesday',
        3: 'Thursday',
        4: 'Friday',
        5: 'Saturday',
        6: 'Sunday'
    }
    date_obj = datetime.datetime.strptime(date_string, '%Y-%m-%d')
    day_of_week_index = date_obj.weekday()
    return days_mapping[day_of_week_index]

if __name__ == '__main__':
    sample_date = '2023-10-05'
    result = get_day_of_week(sample_date)
    print(result)