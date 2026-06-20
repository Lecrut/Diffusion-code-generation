from datetime import datetime, timedelta

def first_day_next_month(date_str):
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    next_month = date_obj.replace(day=28) + timedelta(days=4)
    return next_month.replace(day=1).strftime('%Y-%m-%d')

if __name__ == '__main__':
    print(first_day_next_month('2023-04-15'))