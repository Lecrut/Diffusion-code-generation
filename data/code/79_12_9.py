from datetime import datetime, timedelta

def next_month(date_str):
    date = datetime.strptime(date_str, '%Y-%m-%d')
    next_date = date.replace(day=28) + timedelta(days=4)
    return next_date.strftime('%Y-%m-%d')

if __name__ == '__main__':
    print(next_month('2023-01-15'))