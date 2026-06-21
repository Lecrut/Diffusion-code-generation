from datetime import date, timedelta

def find_next_tuesday(anchor: date) -> date:
    if not isinstance(anchor, date):
        raise ValueError("Anchor must be a date object")
    target_weekday = 1
    current_weekday = anchor.weekday()
    days_ahead = (target_weekday - current_weekday) % 7
    if days_ahead == 0:
        days_ahead = 7
    return anchor + timedelta(days=days_ahead)

if __name__ == '__main__':
    reference_point = date(2023, 7, 4)
    upcoming_tuesday = find_next_tuesday(reference_point)
    print(upcoming_tuesday)