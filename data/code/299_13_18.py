from datetime import date

def is_weekend(day):
    if not isinstance(day, date):
        raise ValueError("Input must be an instance of date")
    return day.weekday() >= 5

if __name__ == '__main__':
    sample_dates = [date(2023, 10, 7), date(2023, 10, 8), date(2023, 10, 9)]
    for sd in sample_dates:
        print(is_weekend(sd))