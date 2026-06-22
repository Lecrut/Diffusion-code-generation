from datetime import datetime, timedelta

def calculate_time_difference(start: datetime, end: datetime) -> timedelta:
    duration_mapping = {
        'standard': lambda s, e: e - s,
        'absolute': lambda s, e: abs(e - s),
        'normalized': lambda s, e: (e - s).total_seconds()
    }
    return duration_mapping['standard'](start, end)

if __name__ == '__main__':
    start_time = datetime(2023, 5, 15, 14, 30, 0)
    end_time = datetime(2023, 5, 15, 10, 15, 0)
    diff = calculate_time_difference(start_time, end_time)
    print(diff)