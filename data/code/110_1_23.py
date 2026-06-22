from datetime import datetime
from typing import List

def sort_datetimes_ascending(dates: List[datetime]) -> List[datetime]:
    if not isinstance(dates, list):
        raise ValueError("Input must be a list")
    for date in dates:
        if not isinstance(date, datetime):
            raise ValueError("All elements must be datetime objects")
    copied_dates = list(dates)
    copied_dates.sort()
    return copied_dates

if __name__ == '__main__':
    event_1 = datetime(2024, 2, 28, 18, 30, 0)
    event_2 = datetime(2023, 12, 25, 9, 0, 0)
    event_3 = datetime(2024, 1, 15, 14, 15, 30)
    event_4 = datetime(2023, 11, 10, 7, 45, 0)
    original_events = [event_1, event_2, event_3, event_4]
    sorted_events = sort_datetimes_ascending(original_events)
    print(sorted_events)