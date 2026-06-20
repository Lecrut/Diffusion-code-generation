from dateutil import parser

day_name_mapping = {
    0: 'Monday',
    1: 'Tuesday',
    2: 'Wednesday',
    3: 'Thursday',
    4: 'Friday',
    5: 'Saturday',
    6: 'Sunday'
}

def get_day_of_week(date_str):
    date_obj = parser.parse(date_str)
    weekday_number = date_obj.weekday()
    return day_name_mapping[weekday_number]

if __name__ == '__main__':
    sample_date = 'January 15, 2023'
    print(get_day_of_week(sample_date))