import calendar
def day_of_year(month, year):
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    if is_leap:
        days_in_month[2] = 29
    cumulative_days = 0
    for m in range(1, month):
        days = days_in_month[m]
        cumulative_days += days
    return cumulative_days + month
if __name__ == '__main__':
    month_val = 2
    year_val = 2024
    result = day_of_year(month_val, year_val)
    print(result)