from datetime import datetime

def compare_iso_dates(date_str1, date_str2):
    try:
        date1 = datetime.fromisoformat(date_str1)
        date2 = datetime.fromisoformat(date_str2)
        return date1 < date2
    except ValueError as e:
        raise ValueError(f"Invalid ISO 8601 date format: {e}")

if __name__ == '__main__':
    print(compare_iso_dates("2023-01-01T12:00:00Z", "2023-01-02T12:00:00Z"))
    print(compare_iso_dates("2023-01-02T12:00:00Z", "2023-01-01T12:00:00Z"))
    try:
        print(compare_iso_dates("2023-01-01T12:00:00", "2023-01-02T12:00:00Z"))
    except ValueError as e:
        print(e)