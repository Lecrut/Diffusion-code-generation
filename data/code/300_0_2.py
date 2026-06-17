import calendar
def calculate_remaining_days(month, year):
    days_in_month = calendar.monthrange(year, month)[1]
    import datetime
    today = datetime.date.today()
    first_day_of_month = datetime.date(year, month, 1)
    if today < first_day_of_month:
        remaining_days = days_in_month - (today.day - 1)
    else:
        remaining_days = days_in_month - (today.day)
    return remaining_days
if __name__ == '__main__':
    target_month = 12
    target_year = 2023
    result = calculate_remaining_days(target_month, target_year)
    print(result)