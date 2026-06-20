from datetime import datetime, timedelta

def next_month_date(date_str):
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    next_month = date_obj.replace(day=28) + timedelta(days=4)
    return next_month.strftime('%Y-%m-%d')

if __name__ == '__main__':
    print(next_month_date('2023-11-15'))