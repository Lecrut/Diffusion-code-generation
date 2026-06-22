from datetime import datetime

def date_difference_in_minutes(date1_str: str, date2_str: str) -> int:
    fmt = '%Y-%m-%d %H:%M:%S'
    dt1 = datetime.strptime(date1_str, fmt)
    dt2 = datetime.strptime(date2_str, fmt)
    delta = dt2 - dt1
    total_seconds = delta.total_seconds()
    return int(total_seconds // 60)

if __name__ == '__main__':
    start_date = '2023-01-01 10:00:00'
    end_date = '2023-01-01 12:30:00'
    result = date_difference_in_minutes(start_date, end_date)
    print(result)