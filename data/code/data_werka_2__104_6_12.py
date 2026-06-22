from datetime import datetime

def compare_dates(date_str1: str, date_str2: str) -> str:
    fmt = "%Y-%m-%d"
    d1 = datetime.strptime(date_str1, fmt)
    d2 = datetime.strptime(date_str2, fmt)
    if d1 < d2:
        return date_str1
    if d1 > d2:
        return date_str2
    return date_str1

if __name__ == '__main__':
    result = compare_dates("2023-01-15", "2023-01-10")
    print(result)