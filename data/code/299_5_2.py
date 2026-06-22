from datetime import datetime

def is_weekend(date_str):
    date = datetime.strptime(date_str, '%Y-%m-%d')
    return date.weekday() >= 5

if __name__ == '__main__':
    dates = ['2023-10-09', '2023-10-10', '2023-10-11']
    results = [is_weekend(date) for date in dates]
    print(results)