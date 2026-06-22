from datetime import datetime

def is_weekend(date_str):
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    return date_obj.weekday() >= 5

if __name__ == '__main__':
    test_dates = ['2023-10-07', '2023-10-08', '2023-10-09']
    for date in test_dates:
        print(f'{date} is weekend: {is_weekend(date)}')