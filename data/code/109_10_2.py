import datetime
def calculate_days_remaining(target_year, target_month, current_year, current_month):
    target_date = datetime.date(target_year, target_month, 1)
    today = datetime.date(current_year, current_month, 1)
    if target_year == current_year:
        if target_month > current_month:
            days = (datetime.date(target_year, target_month, 1) - datetime.date(current_year, current_month, 1)).days
        else:
            days = (datetime.date(target_year, target_month, 1) - datetime.date(current_year, current_month, 1)).days
    else:
        days = (datetime.date(target_year, target_month, 1) - datetime.date(current_year, current_month, 1)).days
    return days
if __name__ == '__main__':
    target_year = 2024
    target_month = 12
    current_year = 2024
    current_month = 10
    days_left = calculate_days_remaining(target_year, target_month, current_year, current_month)
    print(days_left)