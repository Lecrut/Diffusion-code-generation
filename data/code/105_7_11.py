from datetime import datetime, timedelta

def get_upcoming_tuesday(start_date):
    current_date = start_date
    while current_date.weekday() != 1:
        current_date += timedelta(days=1)
    return current_date
if __name__ == '__main__':
    reference_date = datetime(2023, 7, 4)
    upcoming_tuesday = get_upcoming_tuesday(reference_date)
    print(upcoming_tuesday.strftime('%Y-%m-%d'))