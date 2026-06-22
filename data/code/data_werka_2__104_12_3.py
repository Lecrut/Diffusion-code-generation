from datetime import datetime

def get_earlier_iso_date(date_str1: str, date_str2: str) -> str:
    dt1 = datetime.fromisoformat(date_str1)
    dt2 = datetime.fromisoformat(date_str2)
    if dt1 <= dt2:
        return date_str1
    return date_str2

if __name__ == '__main__':
    result = get_earlier_iso_date("2024-01-15T08:30:00", "2024-01-15T08:30:00")
    print(result)