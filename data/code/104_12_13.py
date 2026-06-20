from datetime import datetime

def compare_iso_dates(date_str1, date_str2):
    try:
        dt1 = datetime.fromisoformat(date_str1)
        dt2 = datetime.fromisoformat(date_str2)
        return dt1 < dt2
    except ValueError as e:
        raise ValueError(f"Invalid ISO format: {e}")

if __name__ == '__main__':
    print(compare_iso_dates("2023-04-01T12:00:00", "2023-04-02T12:00:00"))