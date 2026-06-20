from datetime import date

def total_seconds_in_non_leap_year():
    start_date = date(2023, 1, 1)
    end_date = date(2023, 12, 31)
    delta = end_date - start_date
    return delta.total_seconds()

if __name__ == '__main__':
    print(total_seconds_in_non_leap_year())