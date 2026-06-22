from datetime import datetime

def compare_dates(date1: str, date2: str) -> str:
    fmt = "%Y-%m-%d"
    d1 = datetime.strptime(date1, fmt)
    d2 = datetime.strptime(date2, fmt)
    if d1 < d2:
        return "date1 is earlier"
    if d1 > d2:
        return "date2 is earlier"
    return "dates are equal"

if __name__ == '__main__':
    result = compare_dates("2023-01-15", "2023-02-20")
    print(result)