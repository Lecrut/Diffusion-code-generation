from datetime import timedelta

def total_seconds_in_non_leap_year():
    year = 365
    days_in_year = timedelta(days=year)
    seconds_in_year = days_in_year.total_seconds()
    return int(seconds_in_year)

if __name__ == '__main__':
    print(total_seconds_in_non_leap_year())