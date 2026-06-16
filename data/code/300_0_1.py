import calendar
def calculate_remaining_days(month, year):
    days_in_month = calendar.monthrange(year, month)[1]
    import datetime
    today = datetime.date.today()
    first_day_of_month = datetime.date(year, month, 1)
    if today < first_day_of_month:
        return days_in_month - (today.day - 1)
    else:
        return days_in_month - (today.day)
if __name__ == '__main__':
    target_month = 12
    target_year = 2024
    remaining = calculate_remaining_days(target_month, target_year)
    print(remaining)