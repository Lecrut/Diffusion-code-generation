from datetime import datetime

def is_earlier(date_str1, date_str2):
    try:
        date1 = datetime.fromisoformat(date_str1)
        date2 = datetime.fromisoformat(date_str2)
        return date1 < date2
    except ValueError as e:
        raise ValueError(f"Invalid ISO 8601 format: {e}")

if __name__ == '__main__':
    date_a = "2023-05-01T09:30:00"
    date_b = "2023-04-30T23:59:59"
    print(is_earlier(date_a, date_b))