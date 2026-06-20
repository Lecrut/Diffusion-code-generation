from datetime import datetime

def calculate_duration(date1: datetime, date2: datetime) -> int:
    return abs((date2 - date1).total_seconds())

if __name__ == '__main__':
    sample_date1 = datetime(2023, 10, 1)
    sample_date2 = datetime(2023, 9, 15)
    print(calculate_duration(sample_date1, sample_date2))