from datetime import datetime

def compare_datetimes(first: datetime, second: datetime) -> str:
    if first < second:
        return 'First is earlier'
    elif first > second:
        return 'Second is earlier'
    else:
        return 'They are equal'

if __name__ == '__main__':
    first_dt = datetime(2023, 1, 1, 12, 0, 0)
    second_dt = datetime(2023, 1, 1, 12, 0, 0)
    result = compare_datetimes(first_dt, second_dt)
    print(result)