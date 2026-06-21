from datetime import date, timedelta

def find_next_tuesday(anchor: date) -> date:
    current_weekday: int = anchor.weekday()
    target_weekday: int = 1
    days_ahead: int = (target_weekday - current_weekday) % 7
    if days_ahead == 0:
        days_ahead = 7
    return anchor + timedelta(days=days_ahead)

if __name__ == '__main__':
    reference_point: date = date(2023, 7, 4)
    upcoming_tuesday: date = find_next_tuesday(reference_point)
    print(upcoming_tuesday)