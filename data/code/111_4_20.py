from datetime import timedelta, datetime

def calculate_seconds_in_non_leap_year():
    days_in_year = 365
    hours_in_day = 24
    minutes_in_hour = 60
    seconds_in_minute = 60
    seconds_per_day = hours_in_day * minutes_in_hour * seconds_in_minute
    total_seconds = days_in_year * seconds_per_day
    return total_seconds

if __name__ == '__main__':
    result = calculate_seconds_in_non_leap_year()
    print(result)