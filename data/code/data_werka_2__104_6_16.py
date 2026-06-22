from datetime import datetime

def compare_dates(date1: str, date2: str) -> str:
    fmt = "%Y-%m-%d"
    dt1 = datetime.strptime(date1, fmt)
    dt2 = datetime.strptime(date2, fmt)
    if dt1 < dt2:
        return date1
    if dt1 > dt2:
        return date2
    return date1

if __name__ == '__main__':
    result = compare_dates("2023-01-01", "2023-01-02")
    print(result)