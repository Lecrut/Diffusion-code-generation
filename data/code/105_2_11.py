from datetime import datetime, timedelta

def get_upcoming_friday(reference_date):
    days_ahead = 4 - reference_date.weekday()
    if days_ahead <= 0:
        days_ahead += 7
    upcoming_friday = reference_date + timedelta(days=days_ahead)
    return upcoming_friday

if __name__ == '__main__':
    reference = datetime(2023, 12, 15)
    result = get_upcoming_friday(reference)
    print(result.strftime('%Y-%m-%d'))