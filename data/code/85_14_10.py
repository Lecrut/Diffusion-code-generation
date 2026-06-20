from datetime import datetime

def weeks_difference(date1: datetime, date2: datetime) -> int:
    delta = abs((date2 - date1).days)
    full_weeks = delta // 7
    return full_weeks

if __name__ == '__main__':
    sample_date1 = datetime(2023, 4, 1)
    sample_date2 = datetime(2023, 6, 15)
    print(weeks_difference(sample_date1, sample_date2))