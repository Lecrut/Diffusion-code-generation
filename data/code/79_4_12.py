from datetime import datetime, timedelta
DAYS_IN_MONTH = 31

def first_day_of_next_month(date_str):
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    next_month = (date_obj.replace(day=DAYS_IN_MONTH) + timedelta(days=2)).replace(day=1)
    return next_month.strftime('%Y-%m-%d')
if __name__ == '__main__':
    sample_date_str = '2023-10-15'
    print(first_day_of_next_month(sample_date_str))