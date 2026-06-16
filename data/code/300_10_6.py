import datetime
def calculate_remaining_days(target_month, target_year):
    current_year = datetime.datetime.now().year
    current_month = datetime.datetime.now().month
    if target_year == current_year and target_month > current_month:
        remaining_months = 12 - target_month + (target_year % 4 == 0 and target_year % 100 != 0 or target_year % 400 == 0) * 1
        if target_month > current_month:
            days_in_current_month = (datetime.date(current_year, current_month + 1, 1) - datetime.date(current_year, current_month, 1)).days
            if target_year == current_year:
                remaining_days = (datetime.date(target_year, target_month + 1, 1) - datetime.date(current_year, current_month, 1)).days
            else:
                pass
    target_date = datetime.date(target_year, target_month, 1)
    if target_year == current_year:
        if target_month > current_month:
            days_remaining = (datetime.date(current_year, 12, 31) - target_date).days + 1
        else:
            days_remaining = (datetime.date(target_year, 12, 31) - target_date).days + 1
    else:
        try:
            days_in_month = (datetime.date(target_year, target_month + 1, 1) - datetime.date(target_year, target_month, 1)).days
        except ValueError:
            if target_month == 12:
                days_in_month = 31
            else:
                days_in_month = 0
        return days_in_month
if __name__ == '__main__':
    target_month = 12
    target_year = 2024
    result = calculate_remaining_days(target_month, target_year)
    print(result)