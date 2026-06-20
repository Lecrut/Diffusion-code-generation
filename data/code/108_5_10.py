from datetime import datetime

def get_day_of_month(date: datetime) -> int:
    if not isinstance(date, datetime):
        raise ValueError("Input must be an instance of datetime")
    return date.day

if __name__ == '__main__':
    sample_date = datetime(2023, 9, 15)
    print(get_day_of_month(sample_date))