import calendar
def calculate_remaining_days(month, year):
    days_in_month = calendar.monthrange(year, month)[1]
    return days_in_month
if __name__ == '__main__':
    month_input = 10
    year_input = 2023
    remaining_days = calculate_remaining_days(month_input, year_input)
    print(remaining_days)