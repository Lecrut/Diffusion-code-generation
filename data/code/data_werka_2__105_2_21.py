from datetime import date, timedelta

def get_upcoming_friday(reference_date):
    days_ahead = 4 - reference_date.weekday()
    if days_ahead <= 0:
        days_ahead += 7
    return reference_date + timedelta(days=days_ahead)

if __name__ == '__main__':
    reference = date(2023, 12, 15)
    result = get_upcoming_friday(reference)
    print(result)