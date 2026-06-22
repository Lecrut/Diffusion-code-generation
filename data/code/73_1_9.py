from datetime import datetime, timedelta

def calculate_time_diff(date_string1: str, date_string2: str) -> timedelta:
    dt1 = datetime.fromisoformat(date_string1)
    dt2 = datetime.fromisoformat(date_string2)
    return dt2 - dt1

if __name__ == '__main__':
    start_date = "2023-01-01T10:00:00"
    end_date = "2023-01-05T15:30:00"
    result = calculate_time_diff(start_date, end_date)
    print(result)