from datetime import datetime, timedelta

def next_multiple_of_7_days():
    start_date = datetime(2024, 1, 1)
    current_date = start_date + timedelta(days=1)
    while (current_date - start_date).days % 7 != 0:
        current_date += timedelta(days=1)
    return current_date

if __name__ == '__main__':
    result = next_multiple_of_7_days()
    print(result)