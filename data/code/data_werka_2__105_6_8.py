from datetime import date, timedelta

def next_multiple_of_7_days():
    start_date = date(2024, 1, 1)
    days_since_start = 0
    current_date = start_date
    while True:
        if days_since_start > 0 and days_since_start % 7 == 0:
            return current_date
        current_date += timedelta(days=1)
        days_since_start += 1

if __name__ == '__main__':
    result = next_multiple_of_7_days()
    print(result)