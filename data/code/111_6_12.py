from datetime import date, timedelta

def get_next_monday(start_date):
    days_until_monday = (7 - start_date.weekday()) % 7
    next_monday = start_date + timedelta(days=days_until_monday)
    return next_monday

if __name__ == '__main__':
    sample_date = date(2023, 9, 10)
    result = get_next_monday(sample_date)
    print(f"Next Monday after {sample_date}: {result}")