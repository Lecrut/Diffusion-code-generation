import datetime

def is_weekend(date_str):
    date = datetime.datetime.strptime(date_str, '%Y-%m-%d')
    return date.weekday() >= 5

if __name__ == '__main__':
    dates = ['2023-10-07', '2023-10-08', '2023-10-09']
    results = {date: is_weekend(date) for date in dates}
    print(results)