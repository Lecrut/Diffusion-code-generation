from datetime import timedelta

def total_seconds_in_non_leap_year():
    year = 2023
    start_date = datetime(year, 1, 1)
    end_date = datetime(year + 1, 1, 1)
    delta = end_date - start_date
    return delta.total_seconds()
if __name__ == '__main__':
    print(total_seconds_in_non_leap_year())