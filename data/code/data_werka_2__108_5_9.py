from datetime import datetime

def get_day_of_month(dt: datetime) -> int:
    return dt.day

if __name__ == '__main__':
    sample_dt = datetime(2023, 10, 25)
    result = get_day_of_month(sample_dt)
    print(result)