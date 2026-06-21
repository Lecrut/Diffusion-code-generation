from datetime import date, timedelta

def find_nearest_upcoming_saturday(reference_date: date) -> date:
    days_ahead = 5 - reference_date.weekday()
    if days_ahead <= 0:
        days_ahead += 7
    return reference_date + timedelta(days=days_ahead)

if __name__ == '__main__':
    reference = date(2023, 11, 1)
    result = find_nearest_upcoming_saturday(reference)
    print(result)