from datetime import datetime

def get_day_of_month(date_time: datetime) -> int:
    return date_time.day

if __name__ == '__main__':
    sample_date = datetime(2023, 10, 5)
    print(get_day_of_month(sample_date))