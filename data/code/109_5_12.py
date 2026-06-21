import datetime

def calculate_remaining_minutes():
    now = datetime.datetime.now()
    year = now.year
    month = now.month
    if month == 12:
        next_month = 1
        next_year = year + 1
    else:
        next_month = month + 1
        next_year = year
    current_time = datetime.datetime(year, month, now.day, now.hour, now.minute, now.second)
    next_month_time = datetime.datetime(next_year, next_month, 1)
    time_difference = next_month_time - current_time
    total_seconds = time_difference.total_seconds()
    remaining_minutes = int(total_seconds / 60)
    return remaining_minutes

if __name__ == '__main__':
    sample_result = calculate_remaining_minutes()
    print(sample_result)