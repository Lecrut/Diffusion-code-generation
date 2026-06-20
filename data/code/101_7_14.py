import datetime

def get_day_of_week(date_string):
    date_obj = datetime.datetime.strptime(date_string, '%Y-%m-%d').date()
    return date_obj.weekday()
if __name__ == '__main__':
    sample_date = '2024-07-04'
    day_index = get_day_of_week(sample_date)
    print(day_index)