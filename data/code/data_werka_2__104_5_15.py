from datetime import datetime

def compare_datetimes(dt1: datetime, dt2: datetime) -> str:
    if dt1 < dt2:
        return 'First is earlier'
    elif dt1 > dt2:
        return 'Second is earlier'
    else:
        return 'They are equal'

if __name__ == '__main__':
    sample_dt1 = datetime(2023, 1, 1, 10, 0, 0)
    sample_dt2 = datetime(2023, 1, 1, 12, 0, 0)
    result = compare_datetimes(sample_dt1, sample_dt2)
    print(result)