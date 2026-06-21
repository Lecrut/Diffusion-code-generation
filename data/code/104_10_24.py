from datetime import date

def compare_dates(first: date, second: date) -> int:
    if not isinstance(first, date) or not isinstance(second, date):
        raise ValueError("Inputs must be datetime.date objects")
    if first > second:
        return 1
    if first < second:
        return -1
    return 0

if __name__ == '__main__':
    d1 = date(2025, 1, 15)
    d2 = date(2025, 1, 10)
    result = compare_dates(d1, d2)
    print(result)