from datetime import datetime

def is_weekend_or_holiday(date_str):
    date = datetime.strptime(date_str, '%Y-%m-%d')
    if date.weekday() >= 5:
        return True
    if date_str == '2023-10-14':
        return True
    return False
if __name__ == '__main__':
    dates = ['2023-10-13', '2023-10-14', '2023-10-15']
    results = [is_weekend_or_holiday(date) for date in dates]
    print(results)