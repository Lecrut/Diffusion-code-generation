from datetime import datetime

def parse_date(date_str):
    try:
        return datetime.fromisoformat(date_str)
    except ValueError as e:
        raise ValueError(f"Invalid ISO 8601 format: {e}")

def compare_dates(date_str1, date_str2):
    date1 = parse_date(date_str1)
    date2 = parse_date(date_str2)
    return date1 < date2

if __name__ == '__main__':
    print(compare_dates("2023-04-01T12:00:00", "2023-04-02T12:00:00"))