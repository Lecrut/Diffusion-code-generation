from datetime import timedelta

def total_seconds_in_non_leap_year():
    year = 2023
    start_date = f"{year}-01-01"
    end_date = f"{year+1}-01-01"
    delta = timedelta(days=365)
    return delta.total_seconds()

if __name__ == '__main__':
    print(total_seconds_in_non_leap_year())