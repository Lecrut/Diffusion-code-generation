from datetime import date, timedelta

def find_next_tuesday(anchor: date) -> date:
    current_weekday: int = anchor.weekday()
    target_weekday: int = 1
    days_offset: int = (target_weekday - current_weekday) % 7
    if days_offset == 0:
        days_offset = 7
    return anchor + timedelta(days=days_offset)

if __name__ == '__main__':
    start: date = date(2023, 7, 4)
    next_tue: date = find_next_tuesday(start)
    print(next_tue)