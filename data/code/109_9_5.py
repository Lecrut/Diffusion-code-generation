import datetime
def calculate_time_remaining(target_month_year, current_date):
    target_date = datetime.date(target_month_year, 1, 1)
    time_difference = target_date - current_date
    return time_difference.days
if __name__ == '__main__':
    target_month_year = 2024
    current_date = datetime.date(2023, 10, 27)
    time_remaining = calculate_time_remaining(target_month_year, current_date)
    print(time_remaining)