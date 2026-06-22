from datetime import datetime, timedelta

def calculate_time_diff(date1_str: str, date2_str: str) -> timedelta:
    t1 = datetime.fromisoformat(date1_str)
    t2 = datetime.fromisoformat(date2_str)
    return t2 - t1

if __name__ == '__main__':
    s1 = "2024-02-10T08:00:00"
    s2 = "2024-02-10T09:15:30"
    res = calculate_time_diff(s1, s2)
    print(res)