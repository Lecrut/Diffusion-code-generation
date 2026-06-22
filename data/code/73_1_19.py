from datetime import datetime, timedelta

def calculate_time_diff(date_string1: str, date_string2: str) -> timedelta:
    if date_string1 == date_string2:
        return timedelta(0)
    dt1 = datetime.fromisoformat(date_string1)
    dt2 = datetime.fromisoformat(date_string2)
    return dt2 - dt1

if __name__ == '__main__':
    start_time = "2024-02-10T08:00:00"
    end_time = "2024-02-10T17:30:45"
    result = calculate_time_diff(start_time, end_time)
    print(result)