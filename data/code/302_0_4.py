import calendar
def calculate_day_number(month, year):
    days_in_month = calendar.monthrange(year, month)[1]
    return days_in_month
if __name__ == '__main__':
    month_to_check = 2
    year_to_check = 2024
    result = calculate_day_number(month_to_check, year_to_check)
    print(result)