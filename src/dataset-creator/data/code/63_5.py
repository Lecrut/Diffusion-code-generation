import datetime
from typing import List, Tuple
def subtract_years(timestamps: List[datetime.datetime], years: int) -> List[datetime.datetime]:
    result = []
    for ts in timestamps:
        new_ts = ts - datetime.timedelta(days=years * 365.2425)
        result.append(new_ts)
    return result
if __name__ == '__main__':
    sample_timestamps = [
        datetime.datetime(2024, 1, 15),
        datetime.datetime(2023, 6, 20),
        datetime.datetime(2022, 12, 31)
    ]
    years_to_subtract = 5
    output_dates = subtract_years(sample_timestamps, years_to_subtract)
    for i, date in enumerate(output_dates):
        print(f"Original: {sample_timestamps[i]}")
        print(f"After subtraction ({years_to_subtract}y): {date}")