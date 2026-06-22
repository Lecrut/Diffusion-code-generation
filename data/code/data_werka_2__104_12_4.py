from datetime import datetime

def compare_iso_dates(date1: str, date2: str) -> str:
    dt1 = datetime.fromisoformat(date1)
    dt2 = datetime.fromisoformat(date2)
    if dt1 < dt2:
        return date1
    if dt2 < dt1:
        return date2
    return date1

if __name__ == '__main__':
    d1 = "2023-10-01T12:00:00"
    d2 = "2023-10-02T12:00:00"
    result = compare_iso_dates(d1, d2)
    print(result)