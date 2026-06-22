import datetime

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def get_day_of_week(year, month, day):
    if month < 1 or month > 12:
        raise ValueError("Invalid month")
    if day < 1 or day > 31:
        raise ValueError("Invalid day")
    date_obj = datetime.date(year, month, day)
    return date_obj.strftime("%A")

if __name__ == '__main__':
    target_year = 2024
    target_month = 2
    target_day = 29
    if is_leap_year(target_year):
        day_name = get_day_of_week(target_year, target_month, target_day)
        print(day_name)
    else:
        print("Not a leap year")