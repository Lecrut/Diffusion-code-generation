from datetime import datetime

def compare_dates(date_str1, date_str2):
    try:
        dt1 = datetime.fromisoformat(date_str1)
        dt2 = datetime.fromisoformat(date_str2)
        return dt1 < dt2
    except ValueError as e:
        raise ValueError("Invalid ISO 8601 date format") from e

if __name__ == '__main__':
    try:
        print(compare_dates('2023-04-01T12:30:00Z', '2023-04-02T12:30:00Z'))
        print(compare_dates('2023-04-02T12:30:00Z', '2023-04-01T12:30:00Z'))
    except ValueError as e:
        print(e)