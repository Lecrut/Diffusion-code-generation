from datetime import datetime, timedelta

def get_next_tuesday(start_date):
    delta = (2 - start_date.weekday()) % 7
    next_tuesday = start_date + timedelta(days=delta)
    return next_tuesday

if __name__ == '__main__':
    reference_date = datetime(2023, 7, 4)
    next_tuesday = get_next_tuesday(reference_date)
    print(next_tuesday.strftime('%Y-%m-%d'))