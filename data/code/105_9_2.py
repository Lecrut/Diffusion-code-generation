from datetime import datetime, timedelta

def get_next_monday(reference_date):
    days_ahead = 0
    if reference_date.weekday() < 0:
        days_ahead = 0
    else:
        days_ahead = (0 - reference_date.weekday()) % 7
    if days_ahead == 0:
        days_ahead = 7
    next_monday = reference_date + timedelta(days=days_ahead)
    return next_monday

if __name__ == '__main__':
    reference_date = datetime(2024, 2, 28)
    result = get_next_monday(reference_date)
    print(result.strftime('%Y-%m-%d'))