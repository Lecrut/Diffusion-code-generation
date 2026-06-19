from datetime import date

def days_between_dates(date1: str, date2: str) -> int:
    d1 = date.fromisoformat(date1)
    d2 = date.fromisoformat(date2)
    delta = abs((d2 - d1).days)
    return delta
if __name__ == '__main__':
    print(days_between_dates('2023-01-01', '2024-02-29'))
    print(days_between_dates('2023-01-01', '2023-12-31'))
    print(days_between_dates('2020-02-28', '2020-02-29'))
    print(days_between_dates('2019-02-28', '2020-02-28'))