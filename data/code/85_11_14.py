import datetime

WEEKS_PER_YEAR = 52
DAYS_PER_WEEK = 7

def calculate_week_difference(date1: datetime.date, date2: datetime.date) -> int:
    diff = abs(date2 - date1)
    return (diff.days // DAYS_PER_WEEK)

if __name__ == '__main__':
    date1 = datetime.date(2023, 1, 1)
    date2 = datetime.date(2023, 1, 8)
    print(calculate_week_difference(date1, date2))

    date1 = datetime.date(2023, 1, 1)
    date2 = datetime.date(2023, 1, 7)
    print(calculate_week_difference(date1, date2))

    date1 = datetime.date(2023, 1, 1)
    date2 = datetime.date(2023, 1, 1)
    print(calculate_week_difference(date1, date2))