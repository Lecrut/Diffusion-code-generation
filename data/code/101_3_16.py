import datetime

def get_weekday(date_string):
    date_obj = datetime.datetime.strptime(date_string, '%Y-%m-%d')
    return date_obj.strftime('%A')

if __name__ == '__main__':
    sample_date = '2023-12-25'
    day_name = get_weekday(sample_date)
    print(day_name)