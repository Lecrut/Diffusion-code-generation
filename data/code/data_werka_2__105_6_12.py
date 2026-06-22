from datetime import date, timedelta

def next_multiple_of_7_days():
    start_date = date(2024, 1, 1)
    current_date = start_date
    while True:
        days_diff = (current_date - start_date).days
        if days_diff > 0 and days_diff % 7 == 0:
            return current_date
        current_date += timedelta(days=1)

if __name__ == '__main__':
    result = next_multiple_of_7_days()
    print(result)