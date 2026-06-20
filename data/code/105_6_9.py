from datetime import datetime, timedelta

def next_multiple_of_7(start_date):
    current_date = start_date
    while True:
        if current_date.day % 7 == 0:
            return current_date
        current_date += timedelta(days=1)

if __name__ == '__main__':
    start_date = datetime(2024, 1, 1)
    print(next_multiple_of_7(start_date))