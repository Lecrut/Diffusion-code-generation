from datetime import datetime, timedelta

def get_upcoming_tuesday():
    reference_date = datetime(2023, 7, 4)
    days_until_tuesday = (6 - reference_date.weekday()) % 7 + 1
    upcoming_tuesday = reference_date + timedelta(days=days_until_tuesday)
    return upcoming_tuesday.strftime('%Y-%m-%d')

if __name__ == '__main__':
    print(get_upcoming_tuesday())