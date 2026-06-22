from datetime import datetime

def is_weekend_or_holiday(date_str):
    date = datetime.strptime(date_str, '%Y-%m-%d')
    day_of_week = date.weekday()
    holidays = {'2023-10-12'}
    return day_of_week >= 5 or date_str in holidays

if __name__ == '__main__':
    print(is_weekend_or_holiday('2023-10-12'))