from datetime import datetime

def compare_dates(date_str1: str, date_str2: str) -> str:
    fmt = "%Y-%m-%d"
    dt1 = datetime.strptime(date_str1, fmt)
    dt2 = datetime.strptime(date_str2, fmt)
    if dt1 < dt2:
        return "earlier"
    elif dt1 > dt2:
        return "later"
    else:
        return "equal"

if __name__ == '__main__':
    result = compare_dates("2023-01-15", "2023-02-20")
    print(result)