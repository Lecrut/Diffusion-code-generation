from datetime import date, timedelta

def find_next_sunday(start_date):
    while start_date.weekday() != 6:
        start_date += timedelta(days=1)
    return start_date
if __name__ == '__main__':
    sample_date = date(2023, 12, 25)
    next_sunday = find_next_sunday(sample_date)
    print(next_sunday)