import datetime
def calculate_remaining_days(target_month, target_year):
    current_year = datetime.datetime.now().year
    current_month = datetime.datetime.now().month
    if target_year == current_year and target_month > current_month:
        remaining_months = 12 - target_month + (target_year % 4 == 0 and target_year % 100 != 0 or target_year % 400 == 0) * 12
        return (365 if not (target_year % 4 == 0 and target_year % 100 != 0 or target_year % 400 == 0) else 366) - (datetime.date(target_year, target_month, 1) - datetime.date(current_year, current_month, 1)).days
    elif target_year < current_year:
        remaining_days = (365 if not (target_year % 4 == 0 and target_year % 100 != 0 or target_year % 400 == 0) else 366) - (datetime.date(target_year, target_month, 1) - datetime.date(current_year, current_month, 1)).days
        return remaining_days
    else:
        remaining_days = (365 if not (target_year % 4 == 0 and target_year % 100 != 0 or target_year % 400 == 0) else 366) - (datetime.date(target_year, target_month, 1) - datetime.date(current_year, current_month, 1)).days
        return remaining_days
if __name__ == '__main__':
    target_month = 12
    target_year = 2024
    result = calculate_remaining_days(target_month, target_year)
    print(result)