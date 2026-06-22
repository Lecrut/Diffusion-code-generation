from datetime import datetime

def is_weekend(date_str):
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    return date_obj.weekday() >= 5

if __name__ == '__main__':
    dates = ['2023-10-06', '2023-10-07', '2023-10-08']
    results = {date: is_weekend(date) for date in dates}
    print(results)