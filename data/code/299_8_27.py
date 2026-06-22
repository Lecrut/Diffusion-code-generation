import datetime

def is_weekend_or_holiday(date_str):
    date = datetime.datetime.strptime(date_str, '%Y-%m-%d')
    weekday = date.weekday()
    holidays = ['2023-10-14']
    return weekday >= 5 or date_str in holidays
if __name__ == '__main__':
    dates_to_check = ['2023-10-13', '2023-10-14', '2023-10-15']
    results = {date: is_weekend_or_holiday(date) for date in dates_to_check}
    print(results)