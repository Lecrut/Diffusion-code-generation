from datetime import datetime, timedelta

def next_multiple_of_7(start_date):
    while True:
        if start_date.weekday() == 0:
            return start_date
        start_date += timedelta(days=1)
if __name__ == '__main__':
    sample_start_date = datetime(2024, 1, 1)
    next_monday = next_multiple_of_7(sample_start_date)
    print(next_monday.strftime('%Y-%m-%d'))