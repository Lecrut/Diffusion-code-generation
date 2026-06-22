from datetime import datetime

def get_day_of_month(dt: datetime) -> int:
    return dt.day

if __name__ == '__main__':
    sample_date = datetime(2023, 10, 15)
    result = get_day_of_month(sample_date)
    print(result)