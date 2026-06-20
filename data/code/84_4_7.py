import datetime

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def get_day_of_year(date_string):
    try:
        date_obj = datetime.datetime.strptime(date_string, '%Y-%m-%d')
        year = date_obj.year
        month = date_obj.month
        day = date_obj.day
        
        if month < 1 or month > 12 or day < 1 or (month == 2 and day > 29) or (month in [4, 6, 9, 11] and day > 30):
            raise ValueError("Invalid date")
        
        days_in_month = [31, 28 if not is_leap_year(year) else 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return sum(days_in_month[:month-1]) + day
    except ValueError as e:
        raise ValueError("Invalid date format") from e

if __name__ == '__main__':
    test_dates = [
        '2023-10-27',
        '2024-01-01',
        '1999-12-31',
        '2023-02-29',
        'invalid-date'
    ]
    for date_str in test_dates:
        try:
            day_num = get_day_of_year(date_str)
            print(f"Date: {date_str}, Day of Year: {day_num}")
        except ValueError as e:
            print(f"Date: {date_str}, Error: {e}")