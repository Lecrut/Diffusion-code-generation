from datetime import datetime, timedelta

def compute_seconds_in_standard_year():
    start_date = datetime(2023, 1, 1)
    next_year_start = start_date + timedelta(days=365)
    duration = next_year_start - start_date
    return int(duration.total_seconds())

if __name__ == '__main__':
    total_seconds = compute_seconds_in_standard_year()
    print(total_seconds)