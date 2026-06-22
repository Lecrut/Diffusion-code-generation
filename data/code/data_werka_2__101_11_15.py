import datetime

def validate_date_inputs(year, month, day):
    if not isinstance(year, int) or not isinstance(month, int) or not isinstance(day, int):
        raise ValueError("Inputs must be integers")
    if month < 1 or month > 12:
        raise ValueError("Month must be between 1 and 12")
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        days_in_month[1] = 29
    if day < 1 or day > days_in_month[month - 1]:
        raise ValueError("Day is out of range for the given month and year")

def get_day_of_week(year, month, day):
    validate_date_inputs(year, month, day)
    date_obj = datetime.date(year, month, day)
    return date_obj.strftime("%A")

if __name__ == '__main__':
    result = get_day_of_week(2023, 10, 10)
    print(result)