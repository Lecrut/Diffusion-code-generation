from datetime import datetime

def get_day_of_month(dt: datetime) -> int:
    return dt.day

if __name__ == '__main__':
    sample_datetime = datetime(2023, 10, 15, 12, 30, 0)
    result = get_day_of_month(sample_datetime)
    print(result)