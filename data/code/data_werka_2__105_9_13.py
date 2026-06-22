from datetime import date, timedelta

DAY_INDEX_MONDAY = 0
DAYS_IN_WEEK = 7
REFERENCE_YEAR = 2024
REFERENCE_MONTH = 2
REFERENCE_DAY = 28

def compute_next_monday(input_date: date) -> date:
    days_offset = (DAY_INDEX_MONDAY - input_date.weekday()) % DAYS_IN_WEEK
    if days_offset == 0:
        days_offset = DAYS_IN_WEEK
    return input_date + timedelta(days=days_offset)

if __name__ == '__main__':
    base_date = date(REFERENCE_YEAR, REFERENCE_MONTH, REFERENCE_DAY)
    next_monday_date = compute_next_monday(base_date)
    print(next_monday_date)