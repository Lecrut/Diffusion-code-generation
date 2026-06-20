from datetime import datetime

def calculate_week_difference(date1: datetime, date2: datetime) -> int:
    delta = abs(date1 - date2)
    return delta.days // 7

if __name__ == '__main__':
    sample_date1 = datetime(2023, 1, 1)
    sample_date2 = datetime(2023, 1, 8)
    print(calculate_week_difference(sample_date1, sample_date2))