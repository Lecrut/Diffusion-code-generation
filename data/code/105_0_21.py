from datetime import date, timedelta

NEXT_MONDAY_TARGET = 0
DAYS_IN_WEEK = 7
DATE_FORMAT = '%Y-%m-%d'

def compute_next_monday(start_date):
    current_weekday = start_date.weekday()
    days_until_target = (NEXT_MONDAY_TARGET - current_weekday) % DAYS_IN_WEEK
    if days_until_target == 0:
        days_until_target = DAYS_IN_WEEK
    result_date = start_date + timedelta(days=days_until_target)
    return result_date

if __name__ == '__main__':
    today = date.today()
    next_monday = compute_next_monday(today)
    print(next_monday.strftime(DATE_FORMAT))