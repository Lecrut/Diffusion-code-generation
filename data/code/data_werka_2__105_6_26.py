from datetime import date, timedelta

DAYS_IN_WEEK = 7
START_DATE = date(2024, 1, 1)

def get_next_weekly_marker(start: date = START_DATE) -> date:
    if start < START_DATE:
        raise ValueError("Start date must be on or after 2024-01-01")
    days_diff = (start - START_DATE).days
    remainder = days_diff % DAYS_IN_WEEK
    if remainder == 0:
        return start + timedelta(days=DAYS_IN_WEEK)
    days_to_add = DAYS_IN_WEEK - remainder
    return start + timedelta(days=days_to_add)

if __name__ == '__main__':
    result = get_next_weekly_marker(START_DATE)
    print(result)