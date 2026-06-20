from datetime import datetime

def compare_dates(date_str1, date_str2):
    try:
        dt1 = datetime.fromisoformat(date_str1)
        dt2 = datetime.fromisoformat(date_str2)
        return dt1 < dt2
    except ValueError as e:
        raise ValueError("Invalid ISO 8601 format") from e

if __name__ == '__main__':
    date1 = "2023-04-01T12:00:00"
    date2 = "2023-04-02T12:00:00"
    print(compare_dates(date1, date2))