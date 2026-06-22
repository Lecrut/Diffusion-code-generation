from datetime import date, timedelta

TUESDAY_INDEX: int = 1
REFERENCE_DATE: date = date(2023, 7, 4)

def find_next_tuesday(anchor: date) -> date:
    current_day: int = anchor.weekday()
    days_offset: int = (TUESDAY_INDEX - current_day) % 7
    if days_offset == 0:
        days_offset = 7
    return anchor + timedelta(days=days_offset)

if __name__ == '__main__':
    result_date: date = find_next_tuesday(REFERENCE_DATE)
    print(result_date)