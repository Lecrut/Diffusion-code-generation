from datetime import datetime

def compare_dates(date_str1: str, date_str2: str) -> str:
    fmt = "%Y-%m-%d"
    dt1 = datetime.strptime(date_str1, fmt)
    dt2 = datetime.strptime(date_str2, fmt)
    if dt1 < dt2:
        return "earlier"
    if dt1 > dt2:
        return "later"
    return "equal"

if __name__ == '__main__':
    result = compare_dates("2023-01-01", "2023-12-31")
    print(result)