from datetime import datetime

def compare_iso_dates(date_str1: str, date_str2: str) -> str:
    dt1 = datetime.fromisoformat(date_str1)
    dt2 = datetime.fromisoformat(date_str2)
    if dt1 < dt2:
        return date_str1
    if dt2 < dt1:
        return date_str2
    return date_str1

if __name__ == '__main__':
    result = compare_iso_dates("2023-10-01T12:00:00", "2023-10-02T12:00:00")
    print(result)