from datetime import date

def weeks_between_dates(date1: date, date2: date) -> int:
    delta = abs((date2 - date1).days)
    return delta // 7

if __name__ == '__main__':
    print(weeks_between_dates(date(2023, 1, 1), date(2023, 2, 14)))