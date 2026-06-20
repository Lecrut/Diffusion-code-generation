from datetime import datetime

DAYS_PER_YEAR = 365

def get_date_difference(date1, date2):
    return abs((date2 - date1).days)

if __name__ == '__main__':
    date_a = datetime(2023, 1, 1)
    date_b = datetime(2023, 1, 10)
    difference = get_date_difference(date_a, date_b)
    print(f"Difference between {date_a.date()} and {date_b.date()}: {difference} days")