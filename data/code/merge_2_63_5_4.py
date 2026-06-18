import datetime
from typing import List
def subtract_years(timestamps: List[datetime.datetime], years_to_subtract: int) -> List[datetime.datetime]:
    return [ts - datetime.timedelta(days=years_to_subtract * 365 + (years_to_subtract // 4)) for ts in timestamps]
if __name__ == '__main__':
    sample_timestamps = [
        datetime.datetime(2023, 1, 1),
        datetime.datetime(2023, 6, 15),
        datetime.datetime(2024, 12, 31)
    ]
    years_to_remove = 5
    result_timestamps = subtract_years(sample_timestamps, years_to_remove)
    print(result_timestamps)