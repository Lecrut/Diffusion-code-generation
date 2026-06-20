from datetime import datetime, timedelta

def next_multiple_of_7(start_date):
    current = start_date
    while True:
        if current.weekday() == 0:
            return current
        current += timedelta(days=1)
if __name__ == '__main__':
    start_date = datetime(2024, 1, 1)
    print(next_multiple_of_7(start_date))