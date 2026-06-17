import datetime
from typing import List
def subtract_years(timestamps: List[datetime.datetime], years_to_subtract: int) -> List[datetime.datetime]:
    return [ts - datetime.timedelta(days=years_to_subtract * 365 + (years_to_subtract % 4)) for ts in timestamps]
if __name__ == '__main__':
    sample_dates = [
        datetime.datetime(2023, 10, 1),
        datetime.datetime(2024, 5, 15),
        datetime.datetime(2025, 7, 20)
    ]
    years_to_remove = 5
    result_dates = subtract_years(sample_dates, years_to_remove)
    print("Original dates:")
    for d in sample_dates:
        print(d.strftime("%Y-%m-%d"))
    print("\nDates after removing", years_to_remove, "years:")
    for d in result_dates:
        print(d.strftime("%Y-%m-%d"))