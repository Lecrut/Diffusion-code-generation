from datetime import datetime, timedelta

def get_next_tuesday(start_date):
    current_day = start_date.weekday()
    days_until_tuesday = (1 + 6 - current_day) % 7
    next_tuesday = start_date + timedelta(days=days_until_tuesday)
    return next_tuesday.strftime('%Y-%m-%d')

if __name__ == '__main__':
    reference_date = datetime(2023, 7, 4)
    print(get_next_tuesday(reference_date))