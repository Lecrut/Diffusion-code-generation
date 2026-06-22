from datetime import datetime

def compare_dates(date_str1: str, date_str2: str) -> str:
    fmt = "%Y-%m-%d"
    dt1 = datetime.strptime(date_str1, fmt)
    dt2 = datetime.strptime(date_str2, fmt)
    if dt1 < dt2:
        return "date1 is earlier"
    if dt1 > dt2:
        return "date2 is earlier"
    return "dates are equal"

if __name__ == '__main__':
    result = compare_dates("2024-05-10", "2024-05-10")
    print(result)