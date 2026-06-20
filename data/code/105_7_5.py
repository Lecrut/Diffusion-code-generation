from datetime import datetime, timedelta

def get_upcoming_tuesday(start_date):
    current = start_date
    while True:
        if current.weekday() == 1:
            return current
        current += timedelta(days=1)
if __name__ == '__main__':
    reference_date = datetime(2023, 7, 4)
    upcoming_tuesday = get_upcoming_tuesday(reference_date)
    print(upcoming_tuesday.strftime('%Y-%m-%d'))