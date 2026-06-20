from datetime import date, timedelta

def next_15th_day():
    start_date = date(2023, 3, 3)
    current_date = start_date
    while True:
        if current_date.day == 15:
            return current_date
        current_date += timedelta(days=1)

if __name__ == '__main__':
    print(next_15th_day())