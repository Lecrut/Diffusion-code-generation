from datetime import date

def days_between_dates(date1: date, date2: date) -> int:
    return abs((date2 - date1).days)

if __name__ == '__main__':
    print(days_between_dates(date(2023, 1, 1), date(2023, 12, 31)))