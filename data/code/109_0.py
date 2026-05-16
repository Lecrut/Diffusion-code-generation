import datetime
def calculate_days_remaining(target_year, target_month, current_year, current_month):
    target_date = datetime.date(target_year, target_month, 1)
    today = datetime.date(current_year, current_month, 1)
    if target_year == current_year and target_month > current_month:
        days = (datetime.date(target_year, target_month, 1) - datetime.date(current_year, current_month, 1)).days
        return days
    elif target_year == current_year and target_month < current_month:
        days = (datetime.date(datetime.date(current_year, current_month, 1) + datetime.timedelta(days=31) - datetime.timedelta(days=31) + 1) - datetime.date(current_year, current_month, 1)).days
        return (datetime.date(current_year, 12, 1) - datetime.date(current_year, target_month, 1)).days + (datetime.date(target_year, target_month, 1) - datetime.date(target_year, 12, 1))
    else:
        days = (datetime.date(target_year, 12, 1) - datetime.date(current_year, current_month, 1)).days + (datetime.date(target_year, target_month, 1) - datetime.date(target_year, 12, 1))
        return (datetime.date(target_year, 12, 1) - datetime.date(current_year, current_month, 1)).days + (datetime.date(target_year, target_month, 1) - datetime.date(target_year, 12, 1))
if __name__ == '__main__':
    target_year = 2024
    target_month = 12
    current_year = 2024
    current_month = 10
    days_remaining = calculate_days_remaining(target_year, target_month, current_year, current_month)
    print(days_remaining)