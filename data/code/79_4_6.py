from datetime import datetime, timedelta

def first_day_of_next_month(date_str):
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    next_month = (date_obj.replace(day=28) + timedelta(days=4)).replace(day=1)
    return next_month.strftime('%Y-%m-%d')

if __name__ == '__main__':
    sample_date = '2023-04-15'
    print(first_day_of_next_month(sample_date))