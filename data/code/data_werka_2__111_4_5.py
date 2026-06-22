from datetime import timedelta

def calculate_seconds_in_non_leap_year():
    days_in_year = 365
    seconds_per_day = 24 * 60 * 60
    total_seconds = days_in_year * seconds_per_day
    return total_seconds

if __name__ == '__main__':
    result = calculate_seconds_in_non_leap_year()
    print(result)