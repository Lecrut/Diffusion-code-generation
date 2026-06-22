from datetime import datetime

def is_weekend_or_holiday(date_str):
    date = datetime.strptime(date_str, '%Y-%m-%d')
    day_of_week = date.weekday()
    return day_of_week >= 5
if __name__ == '__main__':
    dates_to_check = ['2023-10-13', '2023-10-14', '2023-10-15']
    results = {date: is_weekend_or_holiday(date) for date in dates_to_check}
    print(results)