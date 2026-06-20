import datetime

def get_day_of_week(date_string):
    date_obj = datetime.datetime.strptime(date_string, '%Y-%m-%d')
    day_of_week = date_obj.strftime('%A')
    return day_of_week

if __name__ == '__main__':
    sample_date = '2023-10-05'
    result = get_day_of_week(sample_date)
    print(result)