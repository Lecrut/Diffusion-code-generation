import calendar
def calculate_remaining_days(month, year):
    days_in_month = calendar.monthrange(year, month)[1]
    remaining_days = days_in_month - 1
    return remaining_days
if __name__ == '__main__':
    target_month = 10
    target_year = 2023
    result = calculate_remaining_days(target_month, target_year)
    print(result)