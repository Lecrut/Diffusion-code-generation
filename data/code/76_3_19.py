import argparse
from datetime import date

def days_between(date1: date, date2: date) -> int:
    earlier_date = min(date1, date2)
    later_date = max(date1, date2)
    return (later_date - earlier_date).days

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Calculate the difference in days between two dates.')
    parser.add_argument('date1', type=date.fromisoformat, help='The first date in YYYY-MM-DD format')
    parser.add_argument('date2', type=date.fromisoformat, help='The second date in YYYY-MM-DD format')

    args = parser.parse_args()

    result1 = days_between(date(2023, 2, 15), date(2023, 1, 1))
    print(result1)

    result2 = days_between(date(2024, 6, 10), date(2024, 5, 5))
    print(result2)