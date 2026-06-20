from datetime import date, timedelta

def get_upcoming_tuesday(start_date: date) -> date:
    days_until_tuesday = (1 + 6 - start_date.weekday()) % 7
    return start_date + timedelta(days=days_until_tuesday)

if __name__ == '__main__':
    reference_date = date(2023, 7, 4)
    upcoming_tuesday = get_upcoming_tuesday(reference_date)
    print(upcoming_tuesday.strftime('%Y-%m-%d'))