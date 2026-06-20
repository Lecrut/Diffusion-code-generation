from datetime import datetime

def compare_dates(date_str1, date_str2):
    try:
        date_obj1 = datetime.fromisoformat(date_str1)
        date_obj2 = datetime.fromisoformat(date_str2)
        return date_obj1 < date_obj2
    except ValueError as e:
        raise ValueError(f"Invalid ISO 8601 format: {e}")

if __name__ == '__main__':
    print(compare_dates("2023-04-01T12:00:00", "2023-04-02T12:00:00"))