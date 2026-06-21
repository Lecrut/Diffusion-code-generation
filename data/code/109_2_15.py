from datetime import datetime, timedelta

def calculate_remaining_month_time() -> timedelta:
    current_year = 2024
    current_month = 7
    current_day = 15
    current_hour = 14
    current_minute = 30
    current_second = 0

    start_date = datetime(current_year, current_month, 1)

    if current_month == 12:
        next_month_year = current_year + 1
        next_month = 1
    else:
        next_month_year = current_year
        next_month = current_month + 1

    end_date = datetime(next_month_year, next_month, 1) - timedelta(seconds=1)

    now = datetime(current_year, current_month, current_day, current_hour, current_minute, current_second)

    if now < start_date:
        remaining = end_date - start_date
    elif now > end_date:
        remaining = timedelta(0)
    else:
        remaining = end_date - now

    return remaining

if __name__ == '__main__':
    result = calculate_remaining_month_time()
    print(result)