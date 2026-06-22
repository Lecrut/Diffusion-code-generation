from datetime import datetime

def compare_datetimes(first: datetime, second: datetime) -> str:
    if first < second:
        return 'First is earlier'
    if first > second:
        return 'Second is earlier'
    return 'They are equal'

if __name__ == '__main__':
    dt1 = datetime(2023, 1, 1, 12, 0, 0)
    dt2 = datetime(2023, 1, 2, 12, 0, 0)
    result = compare_datetimes(dt1, dt2)
    print(result)