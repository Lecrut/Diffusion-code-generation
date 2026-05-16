import datetime
def calculate_time_remaining(target_date, current_date):
    time_difference = target_date - current_date
    days_remaining = time_difference.days
    return days_remaining
if __name__ == '__main__':
    target_date = datetime.date(2024, 12, 31)
    current_date = datetime.date(2024, 10, 15)
    result = calculate_time_remaining(target_date, current_date)
    print(result)