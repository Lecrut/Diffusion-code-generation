from datetime import datetime, timedelta

def calculate_time_difference(dt1: datetime, dt2: datetime, unit: str = 'seconds') -> float:
    delta = dt2 - dt1
    total_seconds = abs(delta.total_seconds())
    if unit == 'seconds':
        return total_seconds
    if unit == 'minutes':
        return total_seconds / 60
    if unit == 'hours':
        return total_seconds / 3600
    if unit == 'days':
        return total_seconds / 86400
    return total_seconds

if __name__ == '__main__':
    start_time = datetime(2023, 1, 1, 10, 0, 0)
    end_time = datetime(2023, 1, 2, 12, 30, 0)
    result = calculate_time_difference(start_time, end_time, 'hours')
    print(result)