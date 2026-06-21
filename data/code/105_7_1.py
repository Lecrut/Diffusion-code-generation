from datetime import date, timedelta

def get_upcoming_tuesday(reference_date: date) -> date:
    days_ahead = (1 - reference_date.weekday()) % 7
    if days_ahead == 0:
        days_ahead = 7
    return reference_date + timedelta(days=days_ahead)

if __name__ == '__main__':
    ref_date = date(2023, 7, 4)
    result = get_upcoming_tuesday(ref_date)
    print(result)