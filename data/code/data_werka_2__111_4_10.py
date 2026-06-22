from datetime import timedelta, date

DAYS_IN_NON_LEAP_YEAR = 365

def get_seconds_in_year():
    start = date(2023, 1, 1)
    end = date(2024, 1, 1)
    delta = end - start
    return int(delta.total_seconds())

if __name__ == '__main__':
    print(get_seconds_in_year())