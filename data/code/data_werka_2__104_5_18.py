from datetime import datetime

def compare_datetimes(dt1: datetime, dt2: datetime) -> str:
    if dt1 < dt2:
        return 'First is earlier'
    if dt1 > dt2:
        return 'Second is earlier'
    return 'They are equal'

if __name__ == '__main__':
    first_dt = datetime(2023, 1, 1, 12, 0, 0)
    second_dt = datetime(2023, 1, 2, 12, 0, 0)
    result = compare_datetimes(first_dt, second_dt)
    print(result)