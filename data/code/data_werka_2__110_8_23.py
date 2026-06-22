from datetime import date
from typing import List

EVENT_START_YEAR: int = 2020
EVENT_END_YEAR: int = 2024
DEFAULT_EVENT_COUNT: int = 5

def sort_event_dates(raw_events: List[date]) -> List[date]:
    sorted_list: List[date] = sorted(raw_events)
    return sorted_list

def generate_sample_events() -> List[date]:
    samples: List[date] = [
        date(EVENT_END_YEAR, 12, 25),
        date(EVENT_START_YEAR, 1, 1),
        date(2022, 7, 4),
        date(2020, 10, 31),
        date(2023, 1, 1)
    ]
    return samples

if __name__ == '__main__':
    raw_events = generate_sample_events()
    chronological_order = sort_event_dates(raw_events)
    for day in chronological_order:
        print(day)