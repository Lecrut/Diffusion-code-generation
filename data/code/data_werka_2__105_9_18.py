from datetime import date, timedelta

MONDAY_INDEX = 0
DAYS_IN_WEEK = 7
REFERENCE_DATE = date(2024, 2, 28)

def calculate_next_monday(current_date: date) -> date:
    current_weekday = current_date.weekday()
    days_offset = (MONDAY_INDEX - current_weekday) % DAYS_IN_WEEK
    if days_offset == 0:
        days_offset = DAYS_IN_WEEK
    return current_date + timedelta(days=days_offset)

if __name__ == '__main__':
    target = date(2024, 2, 28)
    next_monday = calculate_next_monday(target)
    print(next_monday)