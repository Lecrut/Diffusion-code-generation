from datetime import datetime, timedelta

def next_fifteenth_day():
    start_date = datetime(2023, 3, 3)
    current_date = start_date
    while True:
        if current_date.day == 15:
            return current_date
        current_date += timedelta(days=1)

if __name__ == '__main__':
    print(next_fifteenth_day())