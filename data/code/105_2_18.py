from datetime import date, timedelta

def calculate_next_friday(reference_date):
    reference_datetime = date(2023, 12, 15)
    days_until_friday = (4 - reference_datetime.weekday()) % 7
    if days_until_friday == 0:
        days_until_friday = 7
    return (reference_datetime + timedelta(days=days_until_friday)).strftime('%Y-%m-%d')

if __name__ == '__main__':
    next_friday_date = calculate_next_friday(None)
    print(next_friday_date)