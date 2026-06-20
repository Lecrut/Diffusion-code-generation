from datetime import datetime, timedelta

def next_wednesday(start_date):
    delta = (2 - start_date.weekday()) % 7
    return start_date + timedelta(days=delta)

if __name__ == '__main__':
    sample_date = datetime(2023, 10, 10)
    print(next_wednesday(sample_date))