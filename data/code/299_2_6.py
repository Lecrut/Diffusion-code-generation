from datetime import datetime

def is_weekend(date_str):
    date = datetime.strptime(date_str, '%Y-%m-%d')
    return date.weekday() >= 5

if __name__ == '__main__':
    dates_to_check = ['2023-10-06', '2023-10-07', '2023-10-08']
    results = {date: is_weekend(date) for date in dates_to_check}
    print(results)