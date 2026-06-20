from datetime import date, timedelta

WEEKDAY_FRIDAY = 4

def upcoming_friday(reference_date):
    reference_datetime = date(2023, 12, 15)
    days_until_friday = (WEEKDAY_FRIDAY - reference_datetime.weekday()) % 7
    if days_until_friday == 0:
        days_until_friday = 7
    return (reference_datetime + timedelta(days=days_until_friday)).strftime('%Y-%m-%d')

if __name__ == '__main__':
    sample_date = date(2023, 12, 15)
    next_friday_str = upcoming_friday(sample_date)
    print(next_friday_str)