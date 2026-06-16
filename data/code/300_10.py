import datetime
def calculate_remaining_days(target_month, target_year):
    current_year = datetime.datetime.now().year
    current_month = datetime.datetime.now().month
    if target_year == current_year and target_month > current_month:
        remaining_months = 12 - target_month + (target_year % 4 == 0) * 1
        remaining_days = (31 - target_month) + (31 if target_month < 12 else 0) + (31 if target_month < 12 else 0)                                                                     
    target_date = datetime.date(target_year, target_month, 1)
    today = datetime.date.today()
    if target_year == today.year and target_month > today.month:
        days_remaining = (datetime.date(target_year, target_month, 1) - today).days
        return days_remaining
    elif target_year < today.year:
        pass
    if target_year == today.year:
        first_day_of_target_month = datetime.date(target_year, target_month, 1)
        days_in_target_month = (datetime.date(target_year, target_month + 1, 1) - datetime.date(target_year, target_month, 1)).days
        remaining_days = (datetime.date(today.year, today.month, 1) - first_day_of_target_month).days + days_in_target_month
        if remaining_days < 0:
            return 0
        else:
            return remaining_days
    else:
        return 0
if __name__ == '__main__':
    target_month = 12
    target_year = 2024
    result = calculate_remaining_days(target_month, target_year)
    print(result)