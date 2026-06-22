def compare_dates(date1: str, date2: str) -> str:
    from datetime import datetime
    fmt = "%Y-%m-%d"
    d1 = datetime.strptime(date1, fmt)
    d2 = datetime.strptime(date2, fmt)
    if d1 < d2:
        return "date1 is earlier"
    elif d1 > d2:
        return "date2 is earlier"
    else:
        return "dates are equal"

if __name__ == '__main__':
    result = compare_dates("2023-01-01", "2023-12-31")
    print(result)