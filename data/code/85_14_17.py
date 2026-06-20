from datetime import datetime

WEEKS_PER_DAY = 7

def weeks_difference(date1: datetime, date2: datetime) -> int:
    delta = abs((date2 - date1).days)
    return delta // WEEKS_PER_DAY

if __name__ == '__main__':
    sample_date1 = datetime(2023, 1, 1)
    sample_date2 = datetime(2023, 1, 15)
    print(weeks_difference(sample_date1, sample_date2))