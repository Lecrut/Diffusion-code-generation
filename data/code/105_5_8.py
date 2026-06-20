from datetime import datetime, timedelta

def next_wednesday(start_date):
    if not isinstance(start_date, datetime):
        raise ValueError("Input must be a datetime object")
    days_to_add = (2 - start_date.weekday()) % 7
    return start_date + timedelta(days=days_to_add)

if __name__ == '__main__':
    sample_date = datetime(2023, 10, 10)
    next_wed = next_wednesday(sample_date)
    print(next_wed.strftime("%Y-%m-%d"))