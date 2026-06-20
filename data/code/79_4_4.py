from datetime import datetime, timedelta

def first_day_of_next_month(date_str):
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    if date_obj.month == 12:
        next_month_first_day = datetime(date_obj.year + 1, 1, 1)
    else:
        next_month_first_day = datetime(date_obj.year, date_obj.month + 1, 1)
    return next_month_first_day.strftime('%Y-%m-%d')

if __name__ == '__main__':
    sample_date = '2023-10-15'
    print(first_day_of_next_month(sample_date))