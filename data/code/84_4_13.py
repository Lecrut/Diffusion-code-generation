import datetime

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_before_month(year, month):
    if month <= 2:
        return [0, 31, 59][month]
    elif is_leap_year(year):
        return [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334][month]
    else:
        return [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334][month]

def get_day_of_year(date_string):
    try:
        date_obj = datetime.datetime.strptime(date_string, '%Y-%m-%d')
        year = date_obj.year
        month = date_obj.month
        day = date_obj.day
        return days_before_month(year, month) + day
    except ValueError:
        return None

if __name__ == '__main__':
    test_dates = [
        '2023-10-27',
        '2024-01-01',
        '1999-12-31',
        '2023-02-29',
        'invalid-date'
    ]
    for date_str in test_dates:
        day_num = get_day_of_year(date_str)
        print(f"Date: {date_str}, Day of Year: {day_num}")