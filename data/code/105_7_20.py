from datetime import date, timedelta

def find_next_tuesday(anchor: date) -> date:
    current_weekday: int = anchor.weekday()
    target_weekday: int = 1
    days_to_add: int = (target_weekday - current_weekday) % 7
    if days_to_add == 0:
        days_to_add = 7
    return anchor + timedelta(days=days_to_add)

if __name__ == '__main__':
    reference: date = date(2023, 7, 4)
    upcoming: date = find_next_tuesday(reference)
    print(upcoming)