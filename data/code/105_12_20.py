from datetime import datetime, timedelta

DAYS_IN_WEEK = 7
REFERENCE_DATE_STR = '2023-10-01'
TARGET_WEEKDAY_INDEX = 4

def compute_next_weekday_date(reference_date_str, target_weekday_index):
    reference_date = datetime.strptime(reference_date_str, '%Y-%m-%d')
    current_weekday = reference_date.weekday()
    days_to_add = (target_weekday_index - current_weekday + DAYS_IN_WEEK) % DAYS_IN_WEEK
    if days_to_add == 0 and reference_date.weekday() != target_weekday_index:
        days_to_add = DAYS_IN_WEEK
    next_date = reference_date + timedelta(days=days_to_add)
    return next_date

if __name__ == '__main__':
    computed_date = compute_next_weekday_date(REFERENCE_DATE_STR, TARGET_WEEKDAY_INDEX)
    print(computed_date.strftime('%Y-%m-%d'))