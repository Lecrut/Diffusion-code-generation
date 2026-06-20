from datetime import datetime, timedelta

def get_upcoming_tuesday(start_date):
    target_day = 2
    current_day = start_date.weekday()
    days_until_tuesday = (target_day - current_day) % 7
    if days_until_tuesday == 0:
        days_until_tuesday += 7
    return start_date + timedelta(days=days_until_tuesday)
if __name__ == '__main__':
    reference_date = datetime(2023, 7, 4)
    upcoming_tuesday = get_upcoming_tuesday(reference_date)
    print(upcoming_tuesday.strftime('%Y-%m-%d'))