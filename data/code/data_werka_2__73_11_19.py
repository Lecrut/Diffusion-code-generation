import calendar
import time

def compute_time_delta_hours(point_a, point_b):
    if not isinstance(point_a, (int, float)):
        raise TypeError("point_a must be a numeric Unix timestamp")
    if not isinstance(point_b, (int, float)):
        raise TypeError("point_b must be a numeric Unix timestamp")
    if point_a == point_b:
        return 0.0
    delta_seconds = point_b - point_a
    return delta_seconds / 3600.0

if __name__ == '__main__':
    ts_a = 1700000000
    ts_b = 1700003600
    hours_diff = compute_time_delta_hours(ts_a, ts_b)
    print(hours_diff)