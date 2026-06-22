import datetime

def compare_dates(date_str1: str, date_str2: str) -> str:
    fmt = "%Y-%m-%d"
    d1 = datetime.datetime.strptime(date_str1, fmt)
    d2 = datetime.datetime.strptime(date_str2, fmt)
    if d1 < d2:
        return "first"
    if d1 > d2:
        return "second"
    return "equal"

if __name__ == '__main__':
    result = compare_dates("2023-01-01", "2023-12-31")
    print(result)