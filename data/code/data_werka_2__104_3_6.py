from datetime import date

def diff_days(start: date, end: date) -> int:
    if not isinstance(start, date) or not isinstance(end, date):
        raise ValueError("Both arguments must be date objects")
    delta = end - start
    return delta.days

if __name__ == '__main__':
    start = date(2022, 6, 15)
    end = date(2022, 7, 20)
    days = diff_days(start, end)
    print(days)