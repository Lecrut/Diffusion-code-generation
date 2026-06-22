from datetime import date
from typing import List

EVENT_CATEGORIES = {
    "conference": date(2023, 11, 15),
    "workshop": date(2022, 5, 20),
    "meetup": date(2024, 1, 10),
    "summit": date(2021, 9, 5),
    "gala": date(2023, 12, 31)
}

def sort_events_by_date(events_dict: dict) -> List[date]:
    event_dates = list(events_dict.values())
    event_dates.sort()
    return event_dates

if __name__ == '__main__':
    raw_events = {
        "conference": date(2023, 11, 15),
        "workshop": date(2022, 5, 20),
        "meetup": date(2024, 1, 10),
        "summit": date(2021, 9, 5),
        "gala": date(2023, 12, 31)
    }
    chronological_dates = sort_events_by_date(raw_events)
    for d in chronological_dates:
        print(d)