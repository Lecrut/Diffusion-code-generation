from datetime import datetime
DAYS_IN_MONTH = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def day_of_year(date_str):
    try:
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')
        year, month, day = (date_obj.year, date_obj.month, date_obj.day)
        if is_leap_year(year) and month > 2:
            return sum(DAYS_IN_MONTH[:month]) + day + 1
        else:
            return sum(DAYS_IN_MONTH[:month]) + day
    except ValueError:
        raise ValueError("Invalid date format. Please use 'YYYY-MM-DD'.")
if __name__ == '__main__':
    print(day_of_year('2023-10-27'))