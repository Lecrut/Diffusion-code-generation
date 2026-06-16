def calculate_day_number(month, year):
    if month == 2:
        is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        if is_leap:
            return 29
        else:
            return 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31
if __name__ == '__main__':
    month_val = 2
    year_val = 2000
    result = calculate_day_number(month_val, year_val)
    print(result)
    month_val = 2
    year_val = 2004
    result = calculate_day_number(month_val, year_val)
    print(result)
    month_val = 1
    year_val = 2023
    result = calculate_day_number(month_val, year_val)
    print(result)
    month_val = 2
    year_val = 2000
    result = calculate_day_number(month_val, year_val)
    print(result)