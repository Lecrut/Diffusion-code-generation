from datetime import datetime, timedelta

def next_wednesday(start_date):
    current_day = start_date.weekday()
    days_until_next_wednesday = (2 - current_day) % 7
    return start_date + timedelta(days=days_until_next_wednesday)

if __name__ == '__main__':
    sample_date = datetime(2023, 10, 10)
    next_wed = next_wednesday(sample_date)
    print(next_wed.strftime("%Y-%m-%d"))