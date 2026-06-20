import datetime
ONE_MONTH = 30

def first_day_of_next_month(date_str):
    date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d')
    next_month_date = date_obj.replace(day=1) + datetime.timedelta(days=ONE_MONTH)
    return next_month_date.replace(day=1).strftime('%Y-%m-%d')
if __name__ == '__main__':
    sample_date_str = '2023-10-15'
    print(first_day_of_next_month(sample_date_str))