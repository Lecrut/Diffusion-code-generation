import datetime

def is_leap_year(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

def calculate_day_of_year(date_tuple):
    year, month, day = date_tuple
    if not (1 <= month <= 12 and 1 <= day <= 31):
        raise ValueError('Invalid date')
    if month == 2 and day > 29:
        raise ValueError('Invalid date for February on a non-leap year')
    if month in [4, 6, 9, 11] and day > 30:
        raise ValueError('Invalid date for April, June, September, or November')
    return (datetime.date(year, month, day) - datetime.date(year, 1, 1)).days + 1
if __name__ == '__main__':
    print(calculate_day_of_year((2024, 3, 15)))
    print(calculate_day_of_year((2000, 1, 1)))
    print(calculate_day_of_year((2023, 12, 31)))
    print(calculate_day_of_year((2024, 2, 29)))
    print(calculate_day_of_year((2023, 1, 1)))