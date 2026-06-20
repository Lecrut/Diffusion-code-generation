from datetime import date, timedelta

def upcoming_friday(reference_date):
    days_until_friday = (4 - reference_date.weekday()) % 7
    return reference_date + timedelta(days=days_until_friday)

if __name__ == '__main__':
    reference_date = date(2023, 12, 15)
    print(upcoming_friday(reference_date))