from datetime import datetime

def get_day_of_month(dt: datetime) -> int:
    if not isinstance(dt, datetime):
        raise ValueError("Expected a datetime object")
    return dt.day

if __name__ == '__main__':
    sample_date = datetime(2024, 2, 29)
    result = get_day_of_month(sample_date)
    print(result)