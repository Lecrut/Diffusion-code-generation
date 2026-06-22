from datetime import timedelta

def calculate_seconds_in_non_leap_year():
    days_in_year = 365
    hours_in_day = 24
    minutes_in_hour = 60
    seconds_in_minute = 60
    total_seconds = days_in_year * hours_in_day * minutes_in_hour * seconds_in_minute
    return total_seconds

if __name__ == '__main__':
    result = calculate_seconds_in_non_leap_year()
    print(result)