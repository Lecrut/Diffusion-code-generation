import calendar
def calculate_day_number(month, year):
    days_in_month = calendar.monthrange(year, month)[1]
    return days_in_month
if __name__ == '__main__':
    month_input = 2
    year_input = 2024
    result = calculate_day_number(month_input, year_input)
    print(result)