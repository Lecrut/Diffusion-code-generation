from datetime import datetime

def compare_dates(date1_str: str, date2_str: str) -> str:
    fmt = "%Y-%m-%d"
    d1 = datetime.strptime(date1_str, fmt)
    d2 = datetime.strptime(date2_str, fmt)
    if d1 < d2:
        return "date1 is earlier"
    if d1 > d2:
        return "date2 is earlier"
    return "dates are equal"

if __name__ == '__main__':
    result = compare_dates("2023-01-01", "2023-12-31")
    print(result)