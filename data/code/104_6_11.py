from datetime import datetime

def compare_dates(date1_str: str, date2_str: str) -> str:
    fmt = "%Y-%m-%d"
    d1 = datetime.strptime(date1_str, fmt)
    d2 = datetime.strptime(date2_str, fmt)
    if d1 < d2:
        return date1_str
    if d1 > d2:
        return date2_str
    return date1_str

if __name__ == '__main__':
    result = compare_dates("2023-01-15", "2023-02-20")
    print(result)