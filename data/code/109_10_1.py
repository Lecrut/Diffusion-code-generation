import datetime
def calculate_days_remaining(target_year, target_month, current_date):
    target_date = datetime.date(target_year, target_month, 1)
    today = current_date
    if target_date > today:
        delta = target_date - today
        return delta.days
    else:
        return 0
if __name__ == '__main__':
    sample_year = 2024
    sample_month = 12
    sample_current_date = datetime.date(2024, 1, 15)
    days_left = calculate_days_remaining(sample_year, sample_month, sample_current_date)
    print(days_left)