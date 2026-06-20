import datetime

DATE_FORMAT = '%Y-%m-%d'

def get_day_of_week(date_string):
    date_obj = datetime.datetime.strptime(date_string, DATE_FORMAT)
    return date_obj.strftime('%A')

if __name__ == '__main__':
    sample_date = '2023-10-05'
    print(get_day_of_week(sample_date))