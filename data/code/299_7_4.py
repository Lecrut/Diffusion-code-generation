def is_weekend_or_holiday(date):
    weekends = {'2023-10-07', '2023-10-08'}
    holidays = {'2023-10-12'}
    return date in weekends or date in holidays

if __name__ == '__main__':
    print(is_weekend_or_holiday('2023-10-12'))