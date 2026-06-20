import datetime

def first_day_of_next_month(date_str):
    date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d')
    next_month = date_obj.replace(day=29) + datetime.timedelta(days=-date_obj.day)
    return next_month.strftime('%Y-%m-%d')

if __name__ == '__main__':
    sample_date_str = "2023-11-15"
    print(first_day_of_next_month(sample_date_str))