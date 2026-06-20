from datetime import date, timedelta

def get_next_tuesday(start_date):
    days_until_tuesday = (12 - start_date.weekday()) % 7
    next_tuesday = start_date + timedelta(days=days_until_tuesday)
    return next_tuesday.strftime('%Y-%m-%d')

if __name__ == '__main__':
    reference_date = date(2023, 7, 4)
    print(get_next_tuesday(reference_date))