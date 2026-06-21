from datetime import datetime

def sort_datetimes(datetimes_list):
    if not datetimes_list:
        return []
    return sorted(datetimes_list)

if __name__ == '__main__':
    sample_datetimes = [
        datetime(2024, 1, 1, 12, 0, 0),
        datetime(2023, 12, 31, 23, 59, 59),
        datetime(2024, 6, 15, 8, 30, 0),
        datetime(2023, 5, 1, 0, 0, 0),
    ]
    result = sort_datetimes(sample_datetimes)
    for dt in result:
        print(dt)