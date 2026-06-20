import datetime

def calculate_remaining_days(current_date):
    target_month_year = current_date.year if current_date.month != 12 else current_date.year + 1
    target_date = datetime.date(target_month_year, 1, 1)
    time_difference = target_date - current_date
    return time_difference.days

if __name__ == '__main__':
    current_date = datetime.date(2024, 6, 1)
    remaining_days = calculate_remaining_days(current_date)
    print(remaining_days)