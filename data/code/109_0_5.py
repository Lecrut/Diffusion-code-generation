import datetime
def calculate_days_remaining(target_year, target_month, current_date):
    target_date = datetime.date(target_year, target_month, 1)
    today = current_date
    if target_date > today:
        delta = target_date - today
        return delta.days
    else:
        delta = today - target_date
        return delta.days
if __name__ == '__main__':
    current_date = datetime.date(2023, 10, 26)
    target_year = 2023
    target_month = 12
    days_left = calculate_days_remaining(target_year, target_month, current_date)
    print(days_left)