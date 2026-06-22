def is_weekend_or_holiday(date):
    weekends = {'2023-10-14'}
    holidays = {'2023-10-13', '2023-10-15'}
    return date in weekends or date in holidays
if __name__ == '__main__':
    print(is_weekend_or_holiday('2023-10-13'))
    print(is_weekend_or_holiday('2023-10-14'))
    print(is_weekend_or_holiday('2023-10-15'))