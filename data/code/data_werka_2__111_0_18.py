from datetime import date, timedelta

def calculate_days_between(start_date, end_date):
    if start_date > end_date:
        return 0
    delta = end_date - start_date
    return delta.days

if __name__ == '__main__':
    start = date(2023, 1, 1)
    end = date(2023, 12, 31)
    result = calculate_days_between(start, end)
    print(result)