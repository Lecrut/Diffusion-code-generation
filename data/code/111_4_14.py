import datetime

SECONDS_PER_MINUTE = 60
MINUTES_PER_HOUR = 60
HOURS_PER_DAY = 24
DAYS_PER_YEAR = 365

def calculate_total_seconds_in_year():
    total_seconds = DAYS_PER_YEAR * HOURS_PER_DAY * MINUTES_PER_HOUR * SECONDS_PER_MINUTE
    return total_seconds

if __name__ == '__main__':
    total_seconds = calculate_total_seconds_in_year()
    print(total_seconds)