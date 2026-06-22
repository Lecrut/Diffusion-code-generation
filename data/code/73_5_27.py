from datetime import datetime, timedelta

def get_time_difference(start: datetime, end: datetime) -> timedelta:
    offset = start - end
    if offset.total_seconds() > 0:
        return -offset
    return offset

if __name__ == '__main__':
    initial = datetime(2024, 6, 15, 9, 30, 0)
    final = datetime(2024, 6, 15, 9, 0, 0)
    diff = get_time_difference(initial, final)
    print(diff)