import datetime
def calculate_remaining_days(target_month, target_year):
    current_year = datetime.datetime.now().year
    current_month = datetime.datetime.now().month
    if target_year == current_year and target_month > current_month:
        remaining_months = 12 - target_month + (target_year % 4 == 0) * 1
        remaining_days = (31 - target_month) + (31 if target_month < 12 else 0) + (31 if target_month < 12 else 0)                                                                     
        try:
            target_date = datetime.date(target_year, target_month, 1)
            today = datetime.date.today()
            if target_year == today.year:
                days_in_target_month = (datetime.date(target_year, target_month + 1, 1) - datetime.date(target_year, target_month, 1)).days
                remaining_days = (datetime.date(target_year, 12, 31) - target_date).days
            else:
                days_in_target_month = (datetime.date(target_year, 12, 31) - datetime.date(target_year, target_month, 1)).days
                remaining_days = days_in_target_month
        except ValueError:
            return "Invalid date input"
    else:
        try:
            if target_year == current_year and target_month >= current_month:
                days_in_target_month = (datetime.date(target_year, target_month + 1, 1) - datetime.date(target_year, target_month, 1)).days
                remaining_days = days_in_target_month
            else:
                days_in_target_month = (datetime.date(target_year, 12, 31) - datetime.date(target_year, target_month, 1)).days
                remaining_days = days_in_target_month
        except ValueError:
            return "Invalid date input"
    today = datetime.date.today()
    target_date_start = datetime.date(target_year, target_month, 1)
    target_date_end = datetime.date(target_year, target_month, 31)                                                  
    if target_month == 12:
        next_month = target_year + 1
        last_day_of_month = datetime.date(next_month, 1, 1) - datetime.timedelta(days=1)
    else:
        next_month = target_year
        last_day_of_month = datetime.date(next_month, target_month + 1, 1) - datetime.timedelta(days=1)
    if last_day_of_month < today:
        return 0
    else:
        remaining = (last_day_of_month - today).days
        return remaining
if __name__ == '__main__':
    target_month = 12
    target_year = 2024
    result = calculate_remaining_days(target_month, target_year)
    print(result)